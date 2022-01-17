from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash
import models.utils_users as utils
from app import app
from oidc_example.op2.client_management import CDB


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


@app.route('/api/get-all-rp', methods=['GET'])
def getall_RP():
    cdb = CDB('..\\client_db')
    return cdb.getall_relyingparty()


if __name__ == "__main__":
    app.run()
