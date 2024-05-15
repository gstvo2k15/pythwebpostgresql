from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    try:
        ip = request.remote_addr
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
