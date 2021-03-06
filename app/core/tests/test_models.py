from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """docstring for ModelTest."""

    def test_create_user_email_successful(self):
        """test creating a new user with an email is successfull"""
        email = 'modshopmsportsbd@gmail.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """test the  email for a new user is normalized"""
        email = 'modshopmsportsbd@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'modshopmsportsbd@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
