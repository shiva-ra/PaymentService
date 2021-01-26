from app.payment_gateways import CheapPaymentGateway, ExpensivePaymentGateway, PremiumPaymentGateway


def process_request(amt):
    """
    As per the business logic appropriate payment method is selected
    :param amt:
    :return: msg to client
    """

    if amt < 20:
        msg = CheapPaymentGateway(amt).process()
    elif 20 <= amt < 500:
        msg = ExpensivePaymentGateway(amt).process()
    else:
        msg = PremiumPaymentGateway(amt).process()

    return msg
