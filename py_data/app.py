import logging
import requests

from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask import send_from_directory

from os import environ

app = Flask(__name__)

@app.route('/manage_file', methods = ['GET'])
def manage_files():
    content = request.get_json()
    if content['action'] == 'download':
        get_external_file()
        return send_from_directory(directory='', path='', filename='sample-text-file.txt')
    elif content['action'] == "read":
        sample_content = read_external_file()
        return jsonify(sample_content), 200
    else:
        return Response(
            "Invalid Request",
            status=400
        )

def get_external_file():
    url = 'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'
    
    sample_text_file = requests.get(url)
    
    with open('sample-text-file.txt', 'wb') as f:
        f.write(sample_text_file.content)
    return 

def read_external_file():
    get_external_file()

    with open('sample-text-file.txt', 'r') as f:
        sample_content = f.read()
    
    return sample_content

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
