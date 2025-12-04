## Put and Delete operations - Http Verbs
## Working with APIs -- JSON data

from flask import Flask, render_template, request, jsonify

app=Flask(__name__)  # Initializing the WSGI and passing parameter which is the entry point of this application


## Initial Data in Todo List
## These datas come from database in real world application
todos = [
    {'id': 1, 'task': 'Buy groceries', 'done': False},
    {'id': 2, 'task': 'Read a book', 'done': False},
    {'id': 3, 'task': 'Go for a walk', 'done': True}
]

@app.route("/")
def home():
    return "<html><H1>Welcome to the Todo List App</H1></html>"
    

## GET - Retrieve all todos items 

@app.route("/todos", methods=['GET'])
def get_todos():
    return jsonify(todos)


## GET - Retrieve a specific todo item by id
@app.route("/todos/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({'message': 'Todo item not found'}), 404
    return jsonify(todo)

## POST - Create a new todo item
@app.route("/todos", methods=['POST'])
def create_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({'message': 'Invalid data'}), 400
    new_todo = { 
        'id': todos[-1]['id'] + 1 if todos else 1,
        'task': request.json['task'],
        'done': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT - Update an existing todo item
@app.route("/todos/<int:todo_id>", methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({'message': 'Todo item not found'}), 404
    if not request.json:
        return jsonify({'message': 'Invalid data'}), 400
    todo['task'] = request.json.get('task', todo['task'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify(todo)

# DELETE - Delete a todo item
@app.route("/todos/<int:todo_id>", methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item['id'] != todo_id]
    return jsonify({'message': 'Todo item deleted'})

if __name__=="__main__":  # This is entry point for any .py file, this is the steps from where the execution starts 
    app.run(debug=True)  # Running the application in debug mode so that any changes made in the code will be reflected without restarting the server

