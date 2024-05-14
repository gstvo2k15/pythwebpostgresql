from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(DISTINCT ip) AS unique_visitors FROM visits;')
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(result)

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

