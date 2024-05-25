"""
App Flask simple para registrar visitas de usuarios y
exponer las métricas a Prometheus.
"""

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Visitor(db.Model):
    """
    Modelo de base de datos para registrar las visitas de los usuarios.
    """
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Visitor {self.ip}>'

    # pylint: disable=too-few-public-methods

@app.before_first_request
def create_tables():
    """
    Crear las tablas de la base de datos antes de la primera solicitud.
    """
    db.create_all()
    # pylint: disable=no-member

@app.route('/')
def index():
    """
    Registra la IP del visitante y retorna el número de visitantes únicos.
    """
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
        new_visitor = Visitor(ip=ip)
        db.session.add(new_visitor)
        db.session.commit()
        unique_visitors = db.session.query(db.func.count(db.distinct(Visitor.ip))).scalar()
        return jsonify(unique_visitors=unique_visitors)
    except ValueError as ve:
        return jsonify(error=str(ve)), 400
    except TypeError as te:
        return jsonify(error=str(te)), 400
    except db.exc.SQLAlchemyError as se:
        return jsonify(error=str(se)), 500
    except Exception as e:  # pylint: disable=broad-exception-caught
        return jsonify(error=str(e)), 500

@app.route('/version')
def version():
    """
    Retorna la versión de la aplicación.
    """
    return jsonify({"version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)