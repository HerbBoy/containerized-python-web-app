import logging
import logging.handlers
import requests

from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from flask import abort

from os import environ

app = Flask(__name__)

# function to handle required tasking defined by project requirements
@app.route('/manage_file', methods = ['GET'])
def manage_files():
    content = request.get_json()

    if content == None:
        abort(500)
        
    elif content['action'] == 'download':
        get_external_file()
        return send_from_directory(directory='', path='', filename='sample-text-file.txt', download_name='sample-text-file.txt', as_attachment=True)

    elif content['action'] == "read":
        sample_content = read_external_file()
        return jsonify(sample_content), 200

    return abort(jsonify(message="Invalid Payload"), 400)

# Leverages request module to run a get request to download a file.    
def get_external_file():
    url = 'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'
    
    sample_text_file = requests.get(url)
    
    with open('sample-text-file.txt', 'wb') as f:
        f.write(sample_text_file.content)
    return 

# Calls function to get file (does this to ensure its present for reading) then provides output back to user.
def read_external_file():
    get_external_file()

    with open('sample-text-file.txt', 'r') as f:
        sample_content = f.read()
    
    return sample_content

# Main function (how when called it executes.)
if __name__ == '__main__':
    #This line ensures it logs to a file if natively run outside of the use of gunicorn
    logging.basicConfig(filename='/var/log/demo.log',level=logging.DEBUG)
    
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
