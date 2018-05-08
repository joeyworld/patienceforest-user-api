import unittest
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from apps.users.models import User
from api.users.views import UserView


class LoginViewTest(TestCase):
    def setUp(self):
        self.email = 'sample@gmail.com'
        self.username = 'John Doe'
        self.password = 'sample_password'
        User.objects.create_user(
            email=self.email,
            password=self.password,
            username=self.username
        )
        self.request = APIRequestFactory()
        self.view = UserView.as_view()
        self.request_body = {
            'email': self.email,
            'username': self.username,
            'password': self.password
        }
        self.response = lambda: self.view(
            self.request.post(
                path='/api/users/login/',
                data=self.request_body,
                format='json'
            )
        )

    @unittest.skip('Test not fully implemented')
    def test_successful_login(self):
        response = self.response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['username'], self.username)
        self.assertIsNotNone(response['token'])

    @unittest.skip('Test not fully implemented')
    def test_login_failure_email_not_provided(self):
        del self.request_body['email']
        self.assertEqual(self.response().status_code, 400)

    @unittest.skip('Test not fully implemented')
    def test_login_failure_incorrect_email_type(self):
        self.request_body['email'] = 'incorrect_email'
        self.assertEqual(self.response().status_code, 400)

    @unittest.skip('Test not fully implemented')
    def test_login_failure_username_not_provided(self):
        del self.request_body['username']
        self.assertEqual(self.response().status_code, 400)

    @unittest.skip('Test not fully implemented')
    def test_login_failure_password_not_provided(self):
        del self.request_body['password']
        self.assertEqual(self.response().status_code, 400)
