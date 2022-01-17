from flask import jsonify, request, Blueprint
from werkzeug.security import generate_password_hash
import models.utils_users as utils


users = Blueprint('users', __name__)


@users.route("/api/users", methods=["GET"])
def get_users():
    rows = utils.get_users()
    data = []
    for r in rows:
        data.append({
            "userid": r[0],
            "username": r[1],
            "password": r[2],
            "email": r[3],
            "admin_flg": r[4],
            "delete_flg": r[5],
        })
    return jsonify({"users": data})


@users.route("/api/user/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = utils.get_user_by_id(user_id)
    data = {
        "userid": user[0],
        "username": user[1],
        "password": user[2],
        "email": user[3],
        "admin_flg": user[4],
        "delete_flg": user[5],
    }

    return jsonify({"user": data})


@users.route("/api/user/<int:userid>", methods=["DELETE"])
def delete_user_by_id(userid):
    user = utils.delete_user_by_id(userid)
    data = {
        "userid": user,
    }

    return jsonify({"userdelete": data})


@users.route("/api/user", methods=["POST"])
def insert_user():
    username = request.json["username"]
    password = generate_password_hash(request.json["password"])
    email = request.json["email"]
    admin_flg = request.json["admin_flg"]
    utils.insert_user_by_id(username, password, email, admin_flg)
    data = {
        "username": username,
    }

    return jsonify({"userinsert": data})


@users.route("/api/user", methods=["PUT"])
def update_user_by_id():
    user_id = request.json["user_id"]
    username = request.json["username"]
    password = generate_password_hash(request.json["password"])
    email = request.json["email"]
    admin_flg = request.json["admin_flg"]
    utils.update_user_by_id(user_id, password, email, admin_flg)
    data = {
        "username": username,
    }

    return jsonify({"userupdate": data})
