from django.test import TestCase
from apps.users.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.email = 'usermodeltest@gmail.com'
        self.username = 'John Doe'
        self.password = 'TestPassWord123'

    def test_create_user_successfully(self):
        created_user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password
        )
        self.assertIsNotNone(created_user.uuid)
        self.assertIsNotNone(created_user.date_joined)
        self.assertFalse(created_user.is_admin)
        self.assertTrue(created_user.is_active)

    def test_create_superuser_successfully(self):
        created_user = User.objects.create_superuser(
            email=self.email,
            username=self.username,
            password=self.password
        )
        self.assertIsNotNone(created_user.uuid)
        self.assertIsNotNone(created_user.date_joined)
        self.assertTrue(created_user.is_admin)
        self.assertTrue(created_user.is_active)

    def test_create_without_email(self):
        self.assertRaises(
            TypeError,
            lambda: User.objects.create_user(
                password=self.password,
                username=self.username
            )
        )

    def test_create_with_nonetype_email(self):
        self.assertRaises(
            ValueError,
            lambda: User.objects.create_user(
                None,
                self.password,
                username=self.username
            )
        )

    def test_create_without_username(self):
        self.assertRaises(
            ValueError,
            lambda: User.objects.create_user(
                self.email,
                self.password
            )
        )

    def test_create_without_password(self):
        self.assertRaises(
            TypeError,
            lambda: User.objects.create_user(
                email=self.email,
                username=self.username
            )
        )
