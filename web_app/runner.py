""" Application router that will serve as the base for the application to be run
All API classes should be built out into their own class
- Those classes exist within web_app/flask_apis
"""

from flask import Flask
from flask_restful import Api
from flask_apis.endpoint_alpha import SampleEndpoint
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

swagger_url = '/swagger-ui'
api_docs = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_docs,
    config={
        'app_name': 'flask_service_template'
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)
api.add_resource(SampleEndpoint, '/v1/endpoint_alpha')

if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')
