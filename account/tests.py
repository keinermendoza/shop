from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth import authenticate

class UsersManagersTests(TestCase):
    def setUp(self):
        """Cretae an User for test_cases of login"""
        User = get_user_model()
        new_user = User.objects.create_user(email="lion@gmail.com", password="lion")
        new_user.username = "greatlion"
        new_user.save()

    def test_create_user(self):
        """test the creation of normal users"""
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")
        
    def test_create_superuser(self):
        """test the creation of superusers"""

        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
       
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False)
    
    def test_login_user_with_email(self):
        """test the login with email"""
        user = authenticate(email="lion@gmail.com", password="lion")
        self.assertTrue(user is not None)
        self.assertEqual(user.username, "greatlion")

    def test_login_user_with_username(self):
        """checks login is not possible using username"""
        user = authenticate(username="greatlion", password="lion")
        self.assertTrue(user is None)
