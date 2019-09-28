import os
from time import time

import pytest

from oic import rndstr
from oic.oic import AccessTokenResponse
from oic.oic.consumer import Consumer
from oic.oic.message import BACK_CHANNEL_LOGOUT_EVENT
from oic.oic.message import AccessTokenRequest
from oic.oic.message import AuthorizationRequest
from oic.oic.message import BackChannelLogoutRequest
from oic.oic.provider import Provider
from oic.utils.authn.authn_context import AuthnBroker
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from oic.utils.authn.client import verify_client
from oic.utils.authn.user import UserAuthnMethod
from oic.utils.authz import AuthzHandling
from oic.utils.jwt import JWT
from oic.utils.keyio import KeyBundle
from oic.utils.keyio import KeyJar
from oic.utils.keyio import keybundle_from_local_file
from oic.utils.sdb import DictSessionBackend
from oic.utils.userinfo import UserInfo

# -- CLIENT INFO ----

CLIENT_ID = "client_1"
ISSUER_ID = "https://example.org"

KC_SYM_S = KeyBundle({"kty": "oct", "key": "abcdefghijklmnop", "use": "sig"})

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/keys"))
KC_RSA = keybundle_from_local_file(
    os.path.join(BASE_PATH, "rsa.key"), "rsa", ["ver", "sig"]
)

CLIKEYS = KeyJar()
CLIKEYS[""] = [KC_RSA, KC_SYM_S]
CLIKEYS[CLIENT_ID] = [KC_RSA, KC_SYM_S]
CLIKEYS[ISSUER_ID] = [KC_RSA]

CONFIG = {
    "authz_page": "authz",
    "scope": ["openid"],
    "response_type": "code",
    # "request_method": "parameter",
    "password": "hemligt",
    "max_age": 3600,
    # "user_info": {"name": None},
}

# Provider information

SERVER_INFO = {
    "version": "3.0",
    "issuer": ISSUER_ID,
    "authorization_endpoint": "https://example.org/authorization",
    "token_endpoint": "https://example.org/token",
    "flows_supported": ["code", "token", "code token"],
}

SRVKEYS = KeyJar()
SRVKEYS[""] = [KC_RSA]
SRVKEYS[CLIENT_ID] = [KC_SYM_S, KC_RSA]
SRVKEYS[ISSUER_ID] = [KC_SYM_S, KC_RSA]

CDB = {
    CLIENT_ID: {
        "password": "hemligt",
        "client_secret": "drickyoughurt",
        "redirect_uris": [("https://example.com/authz", None)],
        "post_logout_redirect_uris": [("https://example.com/post_logout", None)],
        "client_salt": "salted",
        "response_types": ["code"],
    }
}  # type: Dict[str, Dict[str, Any]]

USERDB = {
    "username": {
        "name": "Linda Lindgren",
        "nickname": "Linda",
        "email": "linda@example.com",
        "verified": True,
        "sub": "username",
        "extra_claim": "extra_claim_value",
    }
}

URLMAP = {CLIENT_ID: ["https://example.com/authz"]}


class DummyAuthn(UserAuthnMethod):
    def __init__(self, srv, user):
        UserAuthnMethod.__init__(self, srv)
        self.user = user

    def authenticated_as(self, cookie=None, **kwargs):
        if cookie == "FAIL":
            return None, 0
        else:
            return {"uid": self.user}, time()


AUTHN_BROKER = AuthnBroker()
AUTHN_BROKER.add("UNDEFINED", DummyAuthn(None, "username"))

# dealing with authorization
AUTHZ = AuthzHandling()
SYMKEY = rndstr(16)  # symmetric key used to encrypt cookie info
USERINFO = UserInfo(USERDB)

# AUTHZ request

AREQ = AuthorizationRequest(
    response_type="code",
    client_id=CLIENT_ID,
    redirect_uri="https://example.com/authz",
    scope=["openid"],
    state="state000",
)


class TestOICConsumerLogout:
    @pytest.fixture(autouse=True)
    def setup_consumer(self, session_db_factory):
        client_config = {
            "client_id": CLIENT_ID,
            "client_authn_method": CLIENT_AUTHN_METHOD,
        }

        self.consumer = Consumer(
            DictSessionBackend(), CONFIG, client_config, SERVER_INFO
        )
        self.consumer.keyjar = CLIKEYS
        self.consumer.redirect_uris = ["https://example.com/authz"]
        self.consumer.client_secret = "hemlig"
        self.consumer.secret_type = "basic"
        self.consumer.issuer = ISSUER_ID

        self.provider = Provider(
            ISSUER_ID,
            session_db_factory(ISSUER_ID),
            CDB,
            AUTHN_BROKER,
            USERINFO,
            AUTHZ,
            verify_client,
            SYMKEY,
            urlmap=URLMAP,
            keyjar=SRVKEYS,
        )
        self.provider.baseurl = self.provider.name

    def test_logout(self):
        # Simulate an authorization
        sid, request_location = self.consumer.begin(
            "openid", "code", path="https://example.com"
        )
        resp = self.provider.authorization_endpoint(request=request_location)
        aresp = self.consumer.parse_authz(resp.message)

        assert self.consumer.sdb[sid]["issuer"] == self.provider.baseurl

        # Simulate an accesstoken request
        areq = AccessTokenRequest(
            code=aresp[0]["code"],
            client_id=CLIENT_ID,
            redirect_uri="http://example.com/authz",
            client_secret=self.consumer.client_secret,
            grant_type="authorization_code",
        )
        token_resp = self.provider.code_grant_type(areq)
        tresp = self.consumer.parse_response(
            AccessTokenResponse, token_resp.message, sformat="json"
        )

        # Now, for the backchannel logout. This happens on the OP
        logout_info = {
            "sub": tresp["id_token"]["sub"],
            "events": {BACK_CHANNEL_LOGOUT_EVENT: {}},
        }
        alg = "RS256"
        _jws = JWT(
            self.provider.keyjar,
            iss=self.provider.baseurl,
            lifetime=86400,
            sign_alg=alg,
        )
        _jws.with_jti = True
        logout_token = _jws.pack(aud=CLIENT_ID, **logout_info)

        # The logout request that gets sent to the RP
        request = BackChannelLogoutRequest(logout_token=logout_token)

        # The RP evaluates the request. If everything is OK a session ID (== original state
        # value) is returned.
        _sid = self.consumer.backchannel_logout(request_args=request.to_dict())

        assert _sid == sid