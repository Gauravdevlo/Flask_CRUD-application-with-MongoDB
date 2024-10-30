# app/services/user_service.py
from app import mongo, bcrypt
def create_user(data):
    data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    return mongo.users.insert_one(data)

def get_user_by_id(user_id):
    return mongo.users.find_one({"_id": user_id})

def update_user(user_id, data):
    return mongo.users.update_one({"_id": user_id}, {"$set": data})

def delete_user(user_id):
    return mongo.users.delete_one({"_id": user_id})
