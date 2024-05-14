from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), unique=True)
    visit_time = db.Column(db.DateTime(timezone=True), server_default=func.now())

db.create_all()

@app.route('/')
def index():
    unique_visitors = Visitor.query.count()
    visitors = Visitor.query.all()
    return jsonify({
        'unique_visitors': unique_visitors,
        'visitors': [{'id': v.id, 'ip_address': v.ip_address, 'visit_time': v.visit_time} for v in visitors]
    })

@app.route('/version')
def version():
    return jsonify({'version': '1.0.0'})

@app.before_request
def log_visitor():
    ip_address = request.remote_addr
    if not Visitor.query.filter_by(ip_address=ip_address).first():
        new_visitor = Visitor(ip_address=ip_address)
        db.session.add(new_visitor)
        db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

