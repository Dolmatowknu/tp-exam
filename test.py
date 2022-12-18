import unittest
import app as tapp
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = tapp.app.test_client()

    def test_print_item(self):
#        r = self.app.get('/')
#        self.assertEqual(r._status_code, 200)
        self.assertEqual(tapp.print_item(tapp.box, 'cheese'), '35')

    def test_print_basket_len(self):
#        r = self.app.get('/')
#        self.assertEqual(r._status_code, 200)
        self.assertEqual(tapp.print_basket_len(tapp.box), '5')

if __name__ == '__main__':
    unittest.main()