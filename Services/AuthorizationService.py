#from werkzeug.security import generate_password_hash
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
users = {
    #"user": generate_password_hash("password"),
    "user": "pbkdf2:sha256:260000$hl8kRSxsQIZgK07z$9fa5e07ec2e93d899f44d5bdd615e5e7dad6bced696857c44f6aff328a7793b9"
}
