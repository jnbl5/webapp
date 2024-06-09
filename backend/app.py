from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['34.130.151.4'],
        database=os.environ['myappdb'],
        user=os.environ['jerome'],
        password=os.environ['Lnx!2024']
    )
    return conn

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data['name']
    email = data['email']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id', (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': user_id, 'name': name, 'email': email})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)