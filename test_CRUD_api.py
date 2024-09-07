from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
]

# Get all users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({"users": users}), 200

# Get a single user by ID
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    return jsonify({"user": user}), 200

# Create a new user
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json or not 'email' in request.json:
        abort(400, description="Bad Request: Missing fields")
    
    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": request.json['name'],
        "email": request.json['email']
    }
    users.append(new_user)
    return jsonify({"user": new_user}), 201

# Update an existing user
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    
    if 'name' in request.json:
        user['name'] = request.json['name']
    if 'email' in request.json:
        user['email'] = request.json['email']
    
    return jsonify({"user": user}), 200

# Delete a user
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    
    users.remove(user)
    return jsonify({"result": "User deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
