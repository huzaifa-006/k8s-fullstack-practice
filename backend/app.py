from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv('DATABASE_HOST', 'localhost')
DB_NAME = os.getenv('DATABASE_NAME', 'prescription_db')
DB_USER = os.getenv('DATABASE_USER', 'huzaifa')
DB_PASS = os.getenv('DATABASE_PASSWORD', '1234')

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Flask backend running successfully!"})

@app.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM patients;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients (name, age) VALUES (%s, %s)", (data['name'], data['age']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Patient added!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
