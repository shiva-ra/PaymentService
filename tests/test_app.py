import unittest

from app import create_app


class TestPaymentService(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def test_basic_req(self):
        """
        Testing a very basic request, where the url is correct and all the input data also
        so that it gives 200
        """
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": 50
        })
        self.assertEqual(res.status_code, 200)

    def test_url(self):
        """
        Testing Incorrect URL
        """
        res = self.client().get("/some-url", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": 50
        })
        self.assertEqual(res.status_code, 404)

    def test_ccnum_validation1(self):
        """
        Testing Empty Credit Card Number
        """
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Credit Card Number should be of 16 Digits')

    def test_ccnum_validation2(self):
        """
        Testing Alphabets in Credit Card Number
        """
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "abcdabcdabcdabcd",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Credit Card Number should be of 16 Digits')

    def test_cardholdername(self):
        """ Test Case where Holder name is empty"""
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], "Credit Card Holder's Name cannot be Empty")

    def test_expirationdate1(self):
        """Case where card is expired"""
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/19",
            "SecurityCode": "123",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Your Credit Card has Expired!')

    def test_expirationdate2(self):
        """Case where expiry date does not follow the correct pattern"""
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/2022",
            "SecurityCode": "123",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], "Enter Date in the Format: 'MM/YYYY'")

    def test_securitycode1(self):
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Security Code should be of 3 Digits')

    def test_securitycode2(self):
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "abc",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Security Code should be of 3 Digits')

    def test_securitycode3(self):
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "Amount": 50
        })
        
        self.assertEqual(res.status_code, 200)

    def test_amount1(self):
        """AMount should be above 0"""
        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": 0
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Amount should be greater than 0')

    def test_amount2(self):

        res = self.client().get("/make-payment", data={
            "CreditCardNumber": "1234567891234567",
            "CardHolder": "asd",
            "ExpirationDate": "11/22",
            "SecurityCode": "123",
            "Amount": -200
        })
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()['message'], 'Amount should be greater than 0')
