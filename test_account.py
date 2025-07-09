import unittest
import account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = account.Account("Caitlyn", "222", 10)

    def test_withdraw(self):
        self.setUp()
        self.assertEqual(self.acc.withdraw(5), 5)
        self.assertRaises(ValueError, self.acc.withdraw, 10)
        self.assertEqual(self.acc.current_balance(), 5)

    def test_deposit(self):
        self.setUp()
        self.assertEqual(self.acc.deposit(5), 15)
        self.assertNotEqual(self.acc.deposit(20), 40)
        self.assertEqual(self.acc.current_balance(), 15)

    def test_current_balance(self):
        self.setUp()
        self.assertEqual(self.acc.current_balance(), 10)
        self.assertNotEqual(self.acc.current_balance(), 5)
