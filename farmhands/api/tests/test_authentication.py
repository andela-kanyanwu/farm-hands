from rest_framework.test import APITestCase, APIClient
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class UsersTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='test',
            password='test',
            email='test@test.com'
        )
        self.user.set_password('test')
        self.user.save()

    def tearDown(self):
        User.objects.all().delete()

    # test can login
    def test_login_view(self):
        url = reverse('login')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    # test can logout
    def test_logout_view(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # test can register
    def test_register_view(self):
        url = reverse('register')
        data = {'username': 'tester', 'password': 'tester',
                'email': 'tester@tester.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'username': 'tester',
            'email': 'tester@tester.com'
        })
