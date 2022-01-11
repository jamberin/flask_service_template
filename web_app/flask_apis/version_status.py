""" Endpoint for the versioning and status of the application
- Single endpoint that returns the data of the GIT information
"""

from function.application_status import ApplicationStatus
from flask_restful import Resource
from flask import jsonify

app_status = ApplicationStatus()


class VersionStatus(Resource):
    """ Single status endpoint """

    @staticmethod
    def get():
        """ Return the status of the application """
        content = app_status.generate_status_response()
        return jsonify(content)
