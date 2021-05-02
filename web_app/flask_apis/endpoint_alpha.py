""" Sample endpoint class to show how APIs can be handled using Flask-RESTful
- Single endpoint handling several types
- Query endpoint able to parse some data
- Post endpoint that updates some data with option to delete
- All data should be reset when the application is reset
"""

from flask_restful import Resource
from flask_restful.reqparse import RequestParser

# Example values that can be passed and set
sample_values = {
    15: dict(name='Jerry', role='user'),
    16: dict(name='James', role='admin')
}

# Parser arguments
arg_parse = RequestParser()
arg_parse.add_argument('id', type=int)
arg_parse.add_argument('name', type=str)
arg_parse.add_argument('role', type=str)


class SampleEndpoint(Resource):
    """ Single endpoint that will handle multiple get scenarios """

    @staticmethod
    def get(record_id=None):
        """ Get endpoint to get the sample values """
        if record_id is not None:
            if record_id in sample_values.keys():
                return sample_values[record_id], 200
            else:
                return 'No record with that ID', 404
        return sample_values, 200

    @staticmethod
    def post():
        """ POST a new record to the dict """
        args = arg_parse.parse_args()
        name = args['name']
        role = args['role']
        if name is None or role is None or role not in ['user', 'admin']:
            return 'Name or role incorrect', 400
        keys = []
        for key in sample_values.keys():
            keys.append(key)
        new_key = max(keys) + 1
        sample_values[new_key] = dict(name=name, role=role)
        return 'Created', 201

    @staticmethod
    def put():
        """ Update an existing record """
        args = arg_parse.parse_args()
        name = args['name']
        role = args['role']
        rec_id = args['id']
        if name is None or role is None or role not in ['user', 'admin']:
            return 'Name or role incorrect', 400
        if rec_id not in sample_values.keys():
            return 'Record not found', 404
        sample_values[rec_id] = dict(name=name, role=role)
        return 'Updated', 200

    @staticmethod
    def delete():
        """ Delete an existing record """
        args = arg_parse.parse_args()
        rec_id = args['id']
        if rec_id not in sample_values.keys():
            return 'Record not found', 404
        sample_values.pop(rec_id)
        return 'Removed', 200
