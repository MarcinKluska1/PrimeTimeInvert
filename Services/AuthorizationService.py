from werkzeug.security import generate_password_hash
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
users = {
    "user": generate_password_hash("password"),
}

