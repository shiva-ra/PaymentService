from flask_restful import abort
from datetime import datetime


def validate_creditcardnumber(ccnum):
    """
    It validates the credit card number to be of 16 digits and having only numbers
    """
    if len(ccnum) != 16 or not ccnum.isdigit():
        abort(400, message="Credit Card Number should be of 16 Digits")


def validate_expirationdate(expdate):
    """
    It validates the expiry date in the credit card.
    Accpeted Pattern: MM/YY
    """
    try:
        expdate_datetime = datetime.strptime(expdate, "%m/%y")
        if expdate_datetime < datetime.now():
            abort(400, message="Your Credit Card has Expired!")
    except ValueError:
        abort(400, message="Enter Date in the Format: 'MM/YYYY'")


def validate_securitycode(sc):
    if sc is not None and (len(sc) != 3 or not sc.isdigit()):
        abort(400, message="Security Code should be of 3 Digits")


def validate_cardholder(name):
    if len(name) == 0:
        abort(400, message="Credit Card Holder's Name cannot be Empty")


def validate_amount(amt):
    if amt <= 0:
        abort(400, message="Amount should be greater than 0")


def validate_request(args):
    validate_creditcardnumber(args["CreditCardNumber"])
    validate_cardholder(args["CardHolder"])
    validate_expirationdate(args["ExpirationDate"])
    validate_securitycode(args["SecurityCode"])
    validate_amount(args["Amount"])
