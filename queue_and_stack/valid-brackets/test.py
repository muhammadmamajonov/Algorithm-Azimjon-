import unittest
# from valid_brackets import valid_brackets
from valid_brackets_v2 import valid_brackets


class TestValidBrackets(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(valid_brackets("([{}])"), True)
        self.assertEqual(valid_brackets("[(}]"), False)




if __name__ == "__main__":
    unittest.main()