import os
from flask import Flask, request, send_file
from flasgger import Swagger, LazyJSONEncoder
from flask_restx import Api, Resource
from werkzeug.datastructures import FileStorage
from werkzeug.security import check_password_hash
from Services.PrimeTestService import ValidateNumber
from Services.TimeService import GetTime
from Services.PictureInversionService import InvertImage
from Services.AuthorizationService import users, auth

app = Flask(__name__)
api = Api(app)
app.json_encoder = LazyJSONEncoder
upload_parser = api.parser()
upload_parser.add_argument('file',
                           location='files',
                           type=FileStorage)

swagger = Swagger(app)
ns = api.namespace('', description='SUPER APLIKACJA')

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@ns.route('/prime-test/<int:number>')
@ns.param('number', 'Number to check')
class PrimeTest(Resource):
    def get(self, number):
        """
        Check if number is prime
        """
        return ValidateNumber(number)


@ns.route('/get-time/')
class GetCurrentTime(Resource):
    @auth.login_required
    def get(self):
        """
        Get current time
        """
        return GetTime().__str__()


@ns.route('/picture-inversion/')
@ns.expect(upload_parser)
class PictureInversion(Resource):
    def post(self):
        """
        Picture color inversion
        """
        image = request.files['file']
        return send_file(InvertImage(image), download_name="test.jpg", as_attachment=True)


if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
