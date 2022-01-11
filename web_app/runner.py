""" Application router that will serve as the base for the application to be run
All API classes should be built out into their own class
- Those classes exist within web_app/flask_apis
"""

from flask import Flask
from flask_restful import Api
from flask_apis.endpoint_alpha import SampleEndpoint
from flask_apis.version_status import VersionStatus
from function.application_status import ApplicationStatus

app_status = ApplicationStatus()

app = Flask(__name__)
api = Api(app)

api.add_resource(SampleEndpoint, '/v1/endpoint_alpha')
api.add_resource(VersionStatus, '/adhoc')

if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')
