from misc.dummy_api import hello_world
import unittest


class TestAPI(unittest.TestCase):

    def test_api_returns_200(self):
        response = hello_world()
        print("response: %s" % dir(response))


if __name__ == '__main__':
    #node = ListNode()
    #app.run(debug=True)
    unittest.main()
