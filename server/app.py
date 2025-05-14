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


@app.route('/', methods = ['GET', 'POST', 'REMOVE', 'PATCH'])
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

        # ADD A TASK TO THE DB
        return jsonify({ 'status' : "Success" })

    elif request.method == 'REMOVE':

        # REMOVE A TASK FROM THE DB
        return jsonify({ 'status' : "Success" })
    
    elif request.method == 'PATCH':

        #change status of the id to complete
        return jsonify({ 'status' : "Success" })


if __name__ == '__main__': 
    init_db()
    app.run(debug = True) 