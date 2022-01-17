keys = [
    {"type": "RSA", "key": "cp_keys/key.pem", "use": ["enc", "sig"]},
    {"type": "EC", "crv": "P-256", "use": ["sig"]},
    {"type": "EC", "crv": "P-256", "use": ["enc"]}
]

ISSUER = 'http://localhost'
SERVICE_URL = "{issuer}/verify"

# Only Username and password.
AUTHENTICATION = {
    "UserPassword": {"ACR": "PASSWORD", "WEIGHT": 1, "URL": SERVICE_URL,
                     "END_POINTS": ["verify"]}
}

COOKIENAME = 'pyoic'
COOKIETTL = 4 * 60  # 4 hours
SYM_KEY = "SoLittleTime,Got"

SERVER_CERT = "certs/server.crt"
SERVER_KEY = "certs/server.key"
# CERT_CHAIN="certs/chain.pem"
CERT_CHAIN = None

# =======  SIMPLE DATABASE ==============

USERINFO = "SIMPLE"

USERDB = {
    "phuong": {
        "sub": "phuong0001",
        "name": "Phuong Dao",
        "given_name": "Phuong",
        "family_name": "Dao",
        "nickname": "Phuong",
        "email": "phuong@gmail.com",
        "email_verified": False,
        "phone_number": "+46 90 7865000",
        "MSSV": "20182018",
        "address": {
            "street_address": "Hust",
            "locality": "Bach Khoa",
            "postal_code": "SE-90187",
            "country": "Viet Nam"
        },
    },
    "acc1": {
        "sub": "acc10001",
        "name": "acc1 Account",
        "given_name": "acc1",
        "family_name": "Account",
        "nickname": "acc1",
        "email": "acc1@gmail.com",
        "email_verified": True,
        "MSSV": "20192019",
        "address": {
            "street_address": "40 Ta Quang Buu",
            "locality": "Ta Quang Buu",
            "region": "HN",
            "postal_code": "91608",
            "country": "Viet Nam",
        },
    },
    "acc2": {
        "sub": "acc20001",
        "name": "acc2 Account",
        "given_name": "acc2",
        "family_name": "Account",
        "email": "acc2@gmail.com",
        "email_verified": True,
        "MSSV": "20202020",
        "address": {
            "street_address": "Ta Quang Buu",
            "locality": "Ta Quang Buu",
            "region": "HN",
            "postal_code": "91608",
            "country": "Viet Nam",
        },
    }
}
