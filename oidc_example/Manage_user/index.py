from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash
import models.utils_users as utils
from app import app
from apis import users
from apis import student


app.register_blueprint(users.users)
app.register_blueprint(student.student)


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return make_response('username or password is empty', 400)

    account_password = utils.get_user_by_username(username)

    if not account_password:
        return make_response('Username or password is not available. Try again!', 401)

    if check_password_hash(account_password, password):
        res = {
            'username': username,
        }
        return jsonify(res), 200

    return make_response('Could not verify', 401)


if __name__ == "__main__":
    app.run()
