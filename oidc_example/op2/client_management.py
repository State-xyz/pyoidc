#!/usr/bin/env python
import argparse
import copy
import json
import os
import shelve
import sys
from builtins import input
from typing import Any  # noqa
from typing import List  # noqa
from urllib.parse import parse_qs
from urllib.parse import splitquery  # type: ignore
from urllib.parse import urlparse

from oic import rndstr
from oic.oic.provider import secret
from oic.utils.clientdb import BaseClientDatabase

from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash
import models.utils_users as utils
from app import app

__author__ = "rolandh"


def unpack_redirect_uri(redirect_uris):
    res = []
    for item in redirect_uris:
        (base, query) = item
        if query:
            res.append("%s?%s" % (base, query))
        else:
            res.append(base)
    return res


def pack_redirect_uri(redirect_uris):
    ruri = []
    for uri in redirect_uris:
        if urlparse(uri).fragment:
            print("Faulty redirect uri, contains fragment", file=sys.stderr)
        base, query = splitquery(uri)
        if query:
            ruri.append([base, parse_qs(query)])
        else:
            ruri.append([base, query])

    return ruri


class CDB(BaseClientDatabase):
    """Implementation of ClientDatabase with shelve."""

    def __init__(self, filename):
        self.cdb = shelve.open(filename, writeback=True)
        self.seed = rndstr(32).encode("utf-8")

    def __getitem__(self, item):
        return self.cdb[item]

    def keys(self):
        return self.cdb.keys()

    def items(self):
        return self.cdb.items()

    def create(self, redirect_uris=None, policy_uri="", logo_uri="", jwks_uri=""):
        if redirect_uris is None:
            print("Enter redirect_uris one at the time, end with a blank line: ")
            redirect_uris = []
            while True:
                redirect_uri = input("?: ")
                if redirect_uri:
                    redirect_uris.append(redirect_uri)
                else:
                    break

        client_id = rndstr(12)
        while client_id in self.cdb.keys():
            client_id = rndstr(12)

        client_secret = secret(self.seed, client_id)

        info = {
            "client_secret": client_secret,
            "client_id": client_id,
            "client_salt": rndstr(8),
            "redirect_uris": pack_redirect_uri(redirect_uris),
        }

        if policy_uri:
            info["policy_uri"] = policy_uri
        if logo_uri:
            info["logo_uri"] = logo_uri
        if jwks_uri:
            info["jwks_uri"] = jwks_uri

        self.cdb[client_id] = info

        return self.cdb[client_id]

    def __delitem__(self, key):
        del self.cdb[key]

    def __setitem__(self, key, value):
        self.cdb[key] = eval(value)

    def load(self, filename):
        with open(filename) as f:
            info = json.loads(f.read())
        for item in info:
            if isinstance(item, list):
                self.cdb[str(item[0])] = item[1]
            else:
                _tmp = copy.copy(item)
                try:
                    for uris in ["redirect_uris", "post_logout_redirect_uris"]:
                        try:
                            _tmp[uris] = unpack_redirect_uri(_tmp[uris])
                        except KeyError:
                            pass
                except Exception:
                    print("Faulty specification: {}".format(item))
                else:
                    self.cdb[str(item["client_id"])] = item

    def dump(self, filename):
        res = []  # type: List[Any]
        for key, val in self.cdb.items():
            if isinstance(val, dict):
                res.append(val)
            else:
                res.append([key, val])

        fp = open(filename, "w")
        json.dump(res, fp)
        fp.close()

    def getall_relyingparty(self):
        listRP = []
        for client_id in list(self.keys()):
            client = {}
            redirect_uris = self.cdb[client_id]['redirect_uris'][0][0]
            client['client_id'] = self.cdb[client_id]['client_id']
            client['client_secret'] = self.cdb[client_id]['client_secret']
            client['redirect_uris'] = redirect_uris
            listRP.append(client)
        return listRP

    def get_relyingparty(self, client_id):
        client = {}
        redirect_uris = self.cdb[client_id]['redirect_uris'][0][0]
        client['client_id'] = self.cdb[client_id]['client_id']
        client['client_secret'] = self.cdb[client_id]['client_secret']
        client['redirect_uris'] = redirect_uris
        return client

    def searchrp_by_redirecturi(self, redirect_uri):
        listRP_searched = []
        listRP = self.getall_relyingparty()
        [listRP_searched.append(rp) for rp in listRP if redirect_uri in rp['redirect_uris']]
        return listRP_searched

    def refresh_relyingparty(self, client_id):
        try:
            if client_id not in list(self.keys()):
                return ''
            else:
                redirect_uris = self.cdb[client_id]['redirect_uris'][0][0]
            self.delete_relyingparty(client_id)
        except:
            return ''
        return self.addrelyingparty(redirect_uris)

    def addrelyingparty(self, redirect_uris, policy_uri="", logo_uri="", jwks_uri=""):
        try:
            redirect_uri = [redirect_uris]
            client_info = self.create(redirect_uri, policy_uri, logo_uri, jwks_uri)
        except:
            return ''
        return client_info['client_id']

    def delete_relyingparty(self, client_id):
        try:
            if client_id not in list(self.keys()):
                return ''
            del self.cdb[client_id]
        except:
            return ''
        return client_id


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--list", dest="list", action="store_true", help="List all client_ids"
    )
    parser.add_argument(
        "-d",
        "--delete",
        dest="delete",
        action="store_true",
        help="Delete the entity with the given client_id",
    )
    parser.add_argument(
        "-c",
        "--create",
        dest="create",
        action="store_true",
        help=("Create a new client, returns the stored " "information"),
    )
    parser.add_argument(
        "-s",
        "--show",
        dest="show",
        action="store_true",
        help=("Show information connected to a specific" "client_id"),
    )
    parser.add_argument(
        "-i",
        "--client-id",
        dest="client_id",
        help="A client_id on which to do an action",
    )
    parser.add_argument(
        "-r",
        "--replace",
        dest="replace",
        help=(
            "Information that should replace what's there" "about a specific client_id"
        ),
    )
    parser.add_argument(
        "-I",
        "--input-file",
        dest="input_file",
        help="Import client information from a file",
    )
    parser.add_argument(
        "-D",
        "--output-file",
        dest="output_file",
        help="Dump client information to a file",
    )
    parser.add_argument(
        "-R",
        "--reset",
        dest="reset",
        action="store_true",
        help="Reset the database == removing all registrations",
    )
    parser.add_argument(dest="filename")
    args = parser.parse_args()

    if args.reset:
        os.unlink(args.filename)

    cdb = CDB(args.filename)

    if args.list:
        for client_id in list(cdb.keys()):
            print(client_id)
    elif args.client_id:
        if args.delete:
            del cdb[args.client_id]
        elif args.show:
            print(cdb[args.client_id])
        elif args.replace:
            cdb[args.client_id] = args.replace
    elif args.create:
        print(cdb.create())
    elif args.delete or args.show or args.replace:
        print("You have to specify a client_id !")
    elif args.input_file:
        cdb.load(args.input_file)
    elif args.output_file:
        cdb.dump(args.output_file)


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


@app.route('/api/rps', methods=['GET'])
def getall_RP():
    cdb = CDB('client_db')
    return jsonify({"rp": cdb.getall_relyingparty()})


@app.route('/api/rps/<string:client_id>', methods=['GET'])
def get_RP(client_id):
    cdb = CDB('client_db')
    return jsonify({"rp": cdb.get_relyingparty(client_id)})

@app.route('/api/rp', methods=['POST'])
def add_RP():
    try:
        redirect_uris = request.json['redirect_uri']
        policy_uri = request.json['policy_uri'] if request.json['policy_uri'] else ''
        logo_uri = request.json['logo_uri'] if request.json['logo_uri'] else ''
        cdb = CDB('client_db')
    except:
        return make_response('Could not request', 401)
    return jsonify({"client_id": cdb.addrelyingparty(redirect_uris, policy_uri, logo_uri, '')})


@app.route('/api/rp/<string:client_id>', methods=['DELETE'])
def delete_RP(client_id):
    cdb = CDB('client_db')
    return jsonify({"client_id": cdb.delete_relyingparty(client_id)})


@app.route('/api/rp/<string:client_id>', methods=['PUT'])
def refresh_RP(client_id):
    cdb = CDB('client_db')
    return jsonify({"client_id": cdb.refresh_relyingparty(client_id)})


@app.route('/api/rp/<string:redirect_uri>', methods=['GET'])
def searchrp_by_redirecturi(redirect_uri):
    cdb = CDB('client_db')
    return jsonify({"rp": cdb.searchrp_by_redirecturi(redirect_uri)})


if __name__ == "__main__":
    app.run()
