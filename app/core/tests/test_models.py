from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_with_email_successfull(self):
        """Test for creating the user with email successfully"""
        email = "test@pythonreal.co"
        password = "pythonreal"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        """Test the upper case email with lower case email """
        email = "test@PYTHONREAL.COM"
        user = get_user_model().objects.create_user(
            email, "pythonreal"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_error(self):
        """test creating for new user with no email error raise"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pythonreal')

    def test_create_new_super_user(self):
        """Test creating for new superuser"""
        user = get_user_model().objects.create_superuser(
            "testa@pythonreal.co", 'pythonreal'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
