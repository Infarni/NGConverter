import os
import secrets

from flask import Flask, request, send_file
from flask_restful import Resource, Api

from services.converters import convert

from settings import FORMATS, MEDIA_DIR


app = Flask(__name__)
api = Api(app)


class Formats(Resource):
    def get(self):
        return FORMATS


class Convert(Resource):
    def post(self, format: str):
        file = request.files['file']

        if file:
            format_file = file.filename.split('.')[-1]
            file_path = os.path.join(MEDIA_DIR, f'{secrets.token_hex()}.{format_file}')
            file.save(file_path)

            new_path = convert(format, file_path)

            response = send_file(new_path)

            os.remove(file_path)
            os.remove(new_path)

            return response


api.add_resource(Formats, '/')
api.add_resource(Convert, '/convert/<format>')


if __name__ == '__main__':
    if not os.path.exists(MEDIA_DIR):
        os.mkdir(MEDIA_DIR)

    app.run('0.0.0.0', 5000)
