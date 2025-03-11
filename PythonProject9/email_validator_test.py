import unittest
from email_validator import EmailValidator


class TestEmailValidator(unittest.TestCase):

    def setUp(self):
        self.validator = EmailValidator()

    def test_valid_emails(self):
        # Proste, poprawne adresy email
        self.assertTrue(self.validator.is_valid("user@example.com"))
        self.assertTrue(self.validator.is_valid("user.name@example.com"))
        self.assertTrue(self.validator.is_valid("user-name@example.co.uk"))
        self.assertTrue(self.validator.is_valid("user_name@example-site.com"))
        self.assertTrue(self.validator.is_valid("user123@example.com"))

    def test_invalid_emails(self):
        # Adresy bez znaku @
        self.assertFalse(self.validator.is_valid("userexample.com"))
        
        # Adresy bez nazwy użytkownika
        self.assertFalse(self.validator.is_valid("@example.com"))
        
        # Adresy bez domeny
        self.assertFalse(self.validator.is_valid("user@"))
        
        # Adresy z wieloma znakami @
        self.assertFalse(self.validator.is_valid("user@example@com"))
        
        # Adresy bez .com, .org, itp.
        self.assertFalse(self.validator.is_valid("user@example"))
        
        # Adresy z nieprawidłowymi znakami
        self.assertFalse(self.validator.is_valid("user*name@example.com"))
        self.assertFalse(self.validator.is_valid("user name@example.com"))
        
        # Pusta wartość
        self.assertFalse(self.validator.is_valid(""))
        
        # None
        self.assertFalse(self.validator.is_valid(None))

    def test_domain_validator(self):
        # Test sprawdzania konkretnej domeny
        validator = EmailValidator(allowed_domains=["example.com", "company.org"])
        self.assertTrue(validator.is_valid("user@example.com"))
        self.assertTrue(validator.is_valid("user@company.org"))
        self.assertFalse(validator.is_valid("user@other-site.com"))

    def test_normalize_email(self):
        # Testowanie normalizacji email (usuwanie białych znaków, małe litery)
        self.assertEqual(
            self.validator.normalize("  User@Example.COM  "),
            "user@example.com"
        )
        
        # Test dla None
        self.assertIsNone(self.validator.normalize(None))
        
        # Test dla pustego ciągu
        self.assertEqual(self.validator.normalize(""), "")


if __name__ == '__main__':
    unittest.main()