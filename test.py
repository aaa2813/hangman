# Test functions in main.py

import unittest
from hangman import word

class TestWordMethods(unittest.TestCase):

    def setUp(self):
        self.testword = word("Hello, world!")

    def test_invalid_guess(self):
        # Should not deduct HP or change gamestring
        local_string = self.testword.gamestring
        local_HP = self.testword.HP

        self.testword.guess(".") # Special character guess
        self.assertEqual(local_HP, self.testword.HP)
        self.assertEqual(local_string, self.testword.gamestring)

        self.testword.guess(" ") # Space guess
        self.assertEqual(local_HP, self.testword.HP)
        self.assertEqual(local_string, self.testword.gamestring)

        self.testword.guess(" ") # Empty string guess
        self.assertEqual(local_HP, self.testword.HP)
        self.assertEqual(local_string, self.testword.gamestring)
    
    def test_valid_correct_guess(self):
        # Should not deduct HP, internal chars list should change
        local_HP = self.testword.HP

        self.testword.guess("h") # Lowercase letter guess
        self.assertEqual(local_HP, self.testword.HP)
        self.assertNotIn("H", self.testword.chars)

        self.testword.guess("O") # Uppercase letter guess
        self.assertEqual(local_HP, self.testword.HP)
        self.assertNotIn("O", self.testword.chars)

    def test_valid_incorrect_guess(self):
        # Should deduct 1HP, internal chars list should not change
        local_HP = self.testword.HP
        local_chars = self.testword.chars

        self.testword.guess("x") # Lowercase letter guess
        self.assertEqual(local_HP - 1, self.testword.HP)
        self.assertEqual(local_chars, self.testword.chars)

        self.testword.guess("Z") # Uppercase letter guess
        self.assertEqual(local_HP - 2, self.testword.HP)
        self.assertEqual(local_chars, self.testword.chars)




if __name__ == "__main__":
    unittest.main()