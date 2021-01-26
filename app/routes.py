from flask import jsonify
from flask_restful import reqparse, Resource, abort

from app.payment_processing import process_request
from app.validations import validate_request

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("CreditCardNumber", type=str, required=True)
video_put_args.add_argument("CardHolder", type=str, required=True)
video_put_args.add_argument("ExpirationDate", type=str, required=True)
video_put_args.add_argument("SecurityCode", type=str, required=False)
video_put_args.add_argument("Amount", type=float, required=True)


class PaymentProcess(Resource):
    def get(self):
        """
        This is the method for processing the payment in REST api .
        this executes when the client hits the get request
        :return: response to the client
        """

        args = video_put_args.parse_args()

        # all the args passed in the request is validated
        # any failure will send a response of 400 BAD REQUEST
        validate_request(args)

        try:
            # This is the main method which process the request and select the appropriate gateway
            msg = process_request(args["Amount"])
            return jsonify({"message": msg})
        except Exception as e:
            abort(500, message=f"Unknowm Error Occured: {e}")
