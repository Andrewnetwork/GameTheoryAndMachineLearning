import unittest
from Games.Checkers import Checkers

class TestMain(unittest.TestCase):
    def test_construct(self):
        a = Checkers()
        print("Successfully Constructed Checkers Object")

if __name__ == '__main__':
    unittest.main()