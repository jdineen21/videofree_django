from django.test import TestCase, RequestFactory
from faker import Faker

from .forms import SignupForm

class SignupFormValidationTestCase(TestCase):
    def test_fake_user(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
        }
        self.assertTrue(SignupForm(user).is_valid())
    
    # Password Tests
    def test_short_password(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True),
        }
        self.assertFalse(SignupForm(user).is_valid())

    def test_long_password(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=51, special_chars=True, digits=True, upper_case=True, lower_case=True),
        }
        self.assertFalse(SignupForm(user).is_valid())
    
    def test_no_special_chars_password(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True),
        }
        self.assertFalse(SignupForm(user).is_valid())
    
    def test_no_digits_password(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=10, special_chars=True, digits=False, upper_case=True, lower_case=True),
        }
        self.assertFalse(SignupForm(user).is_valid())

    def test_no_upper_case_password(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=10, special_chars=True, digits=True, upper_case=False, lower_case=True),
        }
        self.assertFalse(SignupForm(user).is_valid())
    
    def test_no_lower_case_password(self):
        fake = Faker()
        user = {
            'username': 'hide on bush',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=False),
        }
        self.assertFalse(SignupForm(user).is_valid())
