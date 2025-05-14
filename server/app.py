from flask import Flask, jsonify, request 
import sqlite3

app = Flask(__name__) 

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        body TEXT, 
        priority INTEGER,
        status BOOLEAN)
    ''')
    conn.commit()
    conn.close()


@app.route('/', methods = ['GET', 'POST', 'DELETE', 'PATCH'])
def home(): 

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == 'GET':

        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        tasks_list = [dict(task) for task in tasks]
        return jsonify({ 'data' : tasks_list })
    
    elif request.method == 'POST':

        data = request.get_json()
        task_text = data.get('body')
        task_priority = data.get('priority')
        cursor.execute('INSERT INTO tasks (body, priority, status) VALUES (?, ?, FALSE)', (task_text, task_priority))
        conn.commit()
        conn.close()
        return jsonify({ 'status' : "Success" })

    elif request.method == 'DELETE':

        task_id = request.get_json().get('id')
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id, ))
        conn.commit()
        conn.close()
        return jsonify({ 'status' : "Deleted", "id": task_id })
    
    elif request.method == 'PATCH':

        data = request.get_json()
        task_id = data.get('id')

        fields = []
        vals = []

        if 'status' in data:
            fields.append('status = ?')
            vals.append(data['status'])
        if 'body' in data:
            fields.append('body = ?')
            vals.append(data['body'])
        if 'priority' in data:
            fields.append('priority = ?')
            vals.append(data['priority'])

        if not fields:
            conn.close()
            return jsonify({ 'error': 'No fields to update' }), 400
        
        vals.append(task_id)
        
        query = f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, vals)
        conn.commit()

        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        updated_task = dict(cursor.fetchone())
        conn.close()
        return jsonify({'message': 'Updated', 'task': updated_task})



if __name__ == '__main__': 
    init_db()
    app.run(debug = True) 