import unittest

from app.payment_gateways import PaymentGateway
from app.payment_processing import process_request


class TestPaymentServiceGateway(unittest.TestCase):
    """
    Since we have imitated real life scenarios, so that any transaction can success or fail
    Which is vey difficult to test, so we are setting the probability of the succcess/availabilty according to our use
    """

    def test_cheappaymentgateway1(self):
        """
        Probability of Success is 1, now no matter what it will not fail. (Same thing goes for availbility)
        """
        PaymentGateway.set_probability_of_success(1)
        msg = process_request(10)
        self.assertEqual(msg, "10 Transaction Successfully via CheapPaymentGateway")

    def test_cheappaymentgateway2(self):
        PaymentGateway.set_probability_of_success(0)
        msg = process_request(5)
        self.assertEqual(msg, "5 Transaction Failed via CheapPaymentGateway")

    def test_expensivepaymentgateway1(self):
        PaymentGateway.set_probability_of_avail(1)
        PaymentGateway.set_probability_of_success(1)
        msg = process_request(25)
        self.assertEqual(msg, "25 Transaction Successfully via ExpensivePaymentGateway")

    def test_expensivepaymentgateway2(self):
        PaymentGateway.set_probability_of_avail(0)
        PaymentGateway.set_probability_of_success(1)
        msg = process_request(25)
        self.assertEqual(msg, "25 Transaction Successfully via CheapPaymentGateway")

    def test_premiumpaymentgateway1(self):
        PaymentGateway.set_probability_of_success(1)
        msg = process_request(2500)
        self.assertEqual(msg, "2500 Transaction Successfully via PremiumPaymentGateway")

    def test_premiumpaymentgateway2(self):
        PaymentGateway.set_probability_of_success(0)
        msg = process_request(2500)
        self.assertEqual(msg, "2500 Transaction Failed via PremiumPaymentGateway")
