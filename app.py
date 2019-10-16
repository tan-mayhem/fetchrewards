from flask import Flask, Blueprint
from flask_restplus import Resource, Api, reqparse
import subprocess

PYRAMID_FILENAME = 'Pyramid'

# method to make app and api and tie them together
def makeapp():

    # create app and api
    app = Flask(__name__)
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp,
              default="FetchRewardsPyramidChallenge",
              default_label="FetchRewardsPyramidChallenge docs")

    # our only endpoint
    @api.route('/pyramidchallenge')
    class pyramidchallenge(Resource):
        ''' Endpoint for Fetch Rewards pyramid coding challenge '''

        # user will POST a string to check
        def post(self):
            '''
            input:    string, string to check if pyramid
            response: "True" if string is pyramid else "False"
            '''
            parser = reqparse.RequestParser()
            parser.add_argument('string', required=True)
            args = parser.parse_args()
            string = args['string']
            
            command = ['java', PYRAMID_FILENAME, string]
            p = subprocess.Popen(command, stdout=subprocess.PIPE)
            text = p.stdout.read()
            retcode = p.wait()
            text = text.decode('utf-8')
            
            return text.replace("\n", "")

    # expose our API through the app
    app.register_blueprint(api_bp)

    return app

if __name__ == '__main__':
    app = makeapp()
    app.debug = True
    app.run()
