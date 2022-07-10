from flask import Flask
from flask_restx import Api

from controller.identification import IdentificationNamespace
from hand_detection.controller import HandDetectionNamespace

app = Flask(__name__)

api = Api(
    app,
    version='1.0', 
    title='test-helper-ai-api', 
    description = 'check test-helper-ai-api'
)

api.add_namespace(IdentificationNamespace, '/identification')
api.add_namespace(HandDetectionNamespace, '/hand-detection')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)