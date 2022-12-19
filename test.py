import unittest
import app as tapp
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = tapp.app.test_client()

    def test_data_split_zero(self):
#        r = self.app.get('/')
#        self.assertEqual(r._status_code, 200)
        self.assertEqual(tapp.data_split_zero(tapp.zero), ['2022', '01', '01'])

#    def test_zero_datatime(self):
#        r = self.app.get('/')
#        self.assertEqual(r._status_code, 200)
#        self.assertEqual(tapp.zero_datatime(tapp.zerosp), 2022-01-01)

    def test_result(self):
        self.assertEqual(tapp.calc(tapp.zerodt, tapp.todaydt), 50)
if __name__ == '__main__':
    unittest.main()