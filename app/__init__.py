from flask import Flask, jsonify
from flask_restful import Api

from app.routes import PaymentProcess


def create_app():
    """
    this is the starting point of our application
    :return: flask app object
    """

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(PaymentProcess, "/make-payment")

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    return app
