# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app import mongo
from app.utils.verification import validate_user_data
user_map= Blueprint("user", __name__)

@user_map.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({"error": message}), 400

    user_id = mongo.users.insert_one(data).inserted_id 
    return jsonify({"id": str(user_id), "message": "User created successfully"}), 201

@user_map.route("/users", methods=["GET"])
def get_users():
    users = []
    for user in mongo.users.find():
        user['_id'] = str(user['_id']) 
        users.append(user)
    return jsonify(users)

@user_map.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = mongo.users.find_one({"_id": ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@user_map.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    result = mongo.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count:
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

@user_map.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = mongo.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404
