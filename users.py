from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock User Data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
]

# Get all users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({"users": users}), 200

# Get user by ID
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify({"user": user}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
