from django.test import TestCase
from rest_framework.test import APIRequestFactory
from apps.users.models import User
from apps.users.views import LoginView, UserCreateView


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
        self.view = LoginView.as_view()
        self.request_body = {
            'email': self.email,
            'password': self.password
        }
        self.response = lambda: self.view(
            self.request.post(
                path='/users/login/',
                data=self.request_body,
                format='json'
            )
        )

    def test_successful_login(self):
        self.assertEqual(self.response().status_code, 200)

    def test_login_failure_email_not_provided(self):
        del self.request_body['email']
        self.assertEqual(self.response().status_code, 400)

    def test_login_failure_incorrect_email_type(self):
        self.request_body['email'] = 'incorrect_email'
        self.assertEqual(self.response().status_code, 400)

    def test_login_failure_incorrect_email(self):
        self.request_body['email'] = 'asdf@gmail.com'
        self.assertEqual(self.response().status_code, 400)

    def test_login_failure_password_not_provided(self):
        del self.request_body['password']
        self.assertEqual(self.response().status_code, 400)

    def test_login_failure_incorrect_password(self):
        self.request_body['password'] = 'incorrect_password'
        self.assertEqual(self.response().status_code, 400)


class UserCreateViewTest(TestCase):
    def setUp(self):
        self.email = 'sample@gmail.com'
        self.username = 'John Doe'
        self.password = 'sample_password'

        self.request = APIRequestFactory()
        self.view = UserCreateView.as_view()
        self.request_body = {
            'email': self.email,
            'username': self.username,
            'password': self.password
        }
        self.response = lambda: self.view(
            self.request.post(
                path='/users/',
                data=self.request_body,
                format='json'
            )
        )

    def test_successful_register(self):
        self.assertEqual(self.response().status_code, 201)

    def test_register_failure_email_not_provided(self):
        del self.request_body['email']
        self.assertEqual(self.response().status_code, 400)

    def test_register_failure_incorrect_email_type(self):
        self.request_body['email'] = 'incorrect_email_type'
        self.assertEqual(self.response().status_code, 400)

    def test_register_failure_duplicate_email(self):
        User.objects.create_user(
            email=self.email,
            password=self.password,
            username=self.username
        )
        self.assertEqual(self.response().status_code, 400)

    def test_register_failure_username_not_provided(self):
        del self.request_body['username']
        self.assertEqual(self.response().status_code, 400)

    def test_register_failure_password_not_provided(self):
        del self.request_body['password']
        self.assertEqual(self.response().status_code, 400)

    def test_register_failure_too_short_password(self):
        self.request_body['password'] = 'short'
        self.assertEqual(self.response().status_code, 400)
