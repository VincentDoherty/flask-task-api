# All /tasks endpoints
from flask import Flask, request, jsonify
import psycopg2

from config import Config

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    )

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks;')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO tasks (title, description, due_date, status) VALUES (%s, %s, %s, %s)',
        (data['title'], data['description'], data['due_date'], data.get('status', 'pending'))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Task created'}), 201

if __name__ == '__main__':
    app.run(debug=True)
