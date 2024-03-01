from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    """
    test a user has a valid user name and a password
    """
    def test_user(self):
        username = 'test-user'
        password = 'psswrd123456'
        u = User(username=username)
        u.set_password(password)
        u.save()
        self.assertEqual(u.username, username)
        self.assertTrue(u.check_password(password))


