from flask import Flask, request

app = Flask(__name__)

todos = []

@app.route('/')
def init():
    return {
        'ok': True
    }

@app.route('/todos', methods=['GET'])
def get_todos():
    return {
        'todos': todos
    }

@app.route('/todos/create', methods=['POST'])
def create_todo():
    req_data = request.get_json()

    new_todo_id = len(todos) + 1

    new_todo = { 'id': new_todo_id, **req_data }

    todos.append(new_todo)
    
    return {
        'ok': True,
    }

@app.route('/todos/delete/<id>', methods=['delete'])
def delete_todo(id):
    task_id = int(id)

    for idx, todo in enumerate(todos):
        if todo.get('id') == task_id:
            todos.pop(idx)
            return {
                'ok': True
            }
    return {
        'ok': False
    }

@app.route('/todos/update/<id>', methods=['PUT'])
def update_todo(id):
    task_id = int(id)
    req_data = request.get_json()

    for idx, todo in enumerate(todos):
        if todo.get('id') == task_id:
            todos.pop(idx)
            todos.insert(idx, { **todo, **req_data })
            break

    return {
        'ok': True
    }
