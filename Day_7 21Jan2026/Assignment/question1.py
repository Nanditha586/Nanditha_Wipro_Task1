from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/")
def home():
    return "This is question 1"
users = [
    {"id": 101, "name": "Nanditha", "email": "nanditha@gmail.com","age":21},
    {"id": 102, "name": "James", "email": "james@gmail.com","age":21},
    {"id": 103, "name": "Sarah", "email": "sarah@gmail.com","age":23},
]

# GET /users → Return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET /users/<id> → Return user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# POST /users → Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"],
        "age": data["age"]
    }

    users.append(new_user)
    return jsonify(new_user), 201

# PUT /users/<id> → Update user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["age"] = data.get("age", user["age"])
            return jsonify({
                "message": "User updated successfully",
                "user": user
            }), 200

    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
