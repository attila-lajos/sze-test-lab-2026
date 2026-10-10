from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
todos = [
    {"id": 1, "task": "Learn TDD", "done": False},
    {"id": 2, "task": "Build a Flask API", "done": True},
]

@app.route('/')
def index():
    return "Welcome"

@app.route('/todos')
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=["POST"])
def post_todos():
    data = request.get_json()
    todos.append({"id": len(todos) + 1, "task": data["task"], "done": False})
    return jsonify(todos), 201

