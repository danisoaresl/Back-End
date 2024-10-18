import unittest

class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one string", "one string")
        
    
class TestAccounts(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(account.create())

    def test_deletion(self):
        self.assertTrue(account.delete())
        
if __name__ == '__main__':
    unittest.main()

