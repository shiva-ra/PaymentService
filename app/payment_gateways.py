from random import choices


class PaymentGateway:
    """
    Parent class for all gateways. It will be inherited by all the gateways
    It plays vital role in Expensive  payment gateway
    """

    # these are class variables used to set probablity of success and availabilty
    # these are manipulated for testing the code, Since these are set using class methods
    p_success = 0.95
    p_avail = 0.92

    def __init__(self, amt):
        self.amt = amt

    @classmethod
    def set_probability_of_success(cls, p_success):
        cls.p_success = p_success

    @classmethod
    def set_probability_of_avail(cls, p_avail):
        cls.p_avail = p_avail

    def is_available(self):
        return choices([True, False], [self.p_avail, 1 - self.p_avail])[0]

    def successful(self):
        return choices([True, False], [self.p_success, 1 - self.p_success])[0]


class CheapPaymentGateway(PaymentGateway):

    def process(self):
        if self.successful():
            return f'{self.amt} Transaction Successfully via CheapPaymentGateway'
        else:
            return f'{self.amt} Transaction Failed via CheapPaymentGateway'


class ExpensivePaymentGateway(PaymentGateway):

    def process(self):

        # if the expensive payment gateway is not available cheap one is selected
        if self.is_available():
            if self.successful():
                return f'{self.amt} Transaction Successfully via ExpensivePaymentGateway'
            else:
                return f'{self.amt} Transaction Failed via ExpensivePaymentGateway'
        else:
            return CheapPaymentGateway(self.amt).process()


class PremiumPaymentGateway(PaymentGateway):

    def process(self):

        count = 0
        retried_success = False
        # this while loop is for 3 times retrial for premium payment method to be successfull
        # which is not there in other payment services, hence the probability of premium gateway is more
        while count < 3 and retried_success is False:
            retried_success = self.successful()
            count += 1

        if retried_success:
            return f'{self.amt} Transaction Successfully via PremiumPaymentGateway'
        else:
            return f'{self.amt} Transaction Failed via PremiumPaymentGateway'
