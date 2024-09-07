from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock Order Data
orders = [
    {"order_id": 1, "user_id": 1, "total": 99.99},
    {"order_id": 2, "user_id": 2, "total": 149.99}
]

# Get all orders
@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders}), 200

# Get orders by user ID
@app.route('/api/v1/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    user = requests.get(f'http://localhost:5001/api/v1/users/{user_id}')
    
    if user.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    user_orders = [order for order in orders if order["user_id"] == user_id]
    return jsonify({"orders": user_orders}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
