#!/usr/local/bin/python3


from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

from package.run_generation import generate_text

application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'


@application.route('/')
def hello_world():
    return "Flask gpt-2 api installed here by ideami"


@application.route('/tellme')
@cross_origin()
def tellme():
    return "Hispania rocks"

@application.route("/generate", methods=['POST'])
@cross_origin()
def get_gen():
    data = request.get_json()

    if 'text' not in data or len(data['text']) == 0 or 'model' not in data:
        abort(400)
    else:
        text = data['text']
        model = data['model']
        
        result =  "I love this: "+text

        #return jsonify({'result': result})

        result = generate_text(
            model_type='gpt2',
            length=100,
            prompt=text,
            model_name_or_path=model
        )

        return jsonify({'result': result})

if __name__ == "__main__":
    #run the application
    application.run(host='0.0.0.0')
