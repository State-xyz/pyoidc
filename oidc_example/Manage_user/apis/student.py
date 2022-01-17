from flask import jsonify, request, Blueprint
import models.utils_students as utils


student = Blueprint('student', __name__)


@student.route("/api/students", methods=["GET"])
def get_users():
    rows = utils.get_users()
    data = []
    for r in rows:
        data.append({
            "userid": r[0],
            "username": r[1],
            "password": r[2],
            "delete_flg": r[3],
        })
    return jsonify({"users": data})


@student.route("/api/student/<string:username>", methods=["GET"])
def get_studentinfo_by_username(username):
    studentinfo = utils.get_studentinfo_by_username(username)
    data = {
        "userid": studentinfo[0],
        "username": studentinfo[1],
        "password": '',
        "student_id": studentinfo[2],
        "sub": studentinfo[3],
        "given_name": studentinfo[4],
        "family_name": studentinfo[5],
        "email": studentinfo[6],
        "address": studentinfo[7],
        "phone_number": studentinfo[8],
        "class_id": studentinfo[9],
    }

    return jsonify({"student": data})


@student.route("/api/student", methods=["PUT"])
def update_user_by_id():
    user_id = request.form["user_id"]
    password = request.form["password"]
    given_name = request.form["given_name"]
    family_name = request.form["family_name"]
    email = request.form["email"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    class_id = request.form["class_id"]
    utils.update_user_by_id(user_id, password, given_name, family_name, email, address,
                            phone_number, class_id)
    data = {
        "userid": user_id,
        "password": '',
        "given_name": given_name,
        "family_name": family_name,
        "email": email,
        "address": address,
        "phone_number": phone_number,
        "class_id": class_id,
    }

    return jsonify({"userupdate": data})
