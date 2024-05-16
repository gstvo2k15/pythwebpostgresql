from flask import Flask, jsonify, request   # The web framework used to build the application.
from flask_sqlalchemy import SQLAlchemy     # An extension for Flask that adds support for SQLAlchemy, a SQL toolkit and ORM.
from prometheus_flask_exporter import PrometheusMetrics # An exporter for Prometheus to gather metrics about the application.
import os # Used to access environment variables.

app = Flask(__name__)     # Initializes a Flask application.      
metrics = PrometheusMetrics(app) # Integrates Prometheus metrics to monitor the application.

# Database Configuration: Configures the SQLAlchemy database URI using an environment variable or a default value.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model: defines a Visitor model with three fields: id, ip, and timestamp.
class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Create Tables
@app.before_first_request
def create_tables():
    db.create_all()

# Create routes
@app.route('/')
def index():
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
        new_visitor = Visitor(ip=ip)
        db.session.add(new_visitor)
        db.session.commit()
        unique_visitors = db.session.query(db.func.count(db.distinct(Visitor.ip))).scalar()
        return jsonify(unique_visitors=unique_visitors)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0"})

# Runs the Flask application on host 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

