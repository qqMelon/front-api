from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import (
    BaseUnicornFactory,
    SimpleUserProfileFactory,
    AdminUserProfileFactory,
    SimpleUserFactory,
    AdminUserFactory,
)
from ..models import Unicorn
from rest_framework.authtoken.models import Token
from django.forms.models import model_to_dict
from ..models import User, Unicorn

class LoginViewTests(APITestCase):
    def setUp(self):
        self.user = SimpleUserFactory()
        self.userProfile = SimpleUserProfileFactory(user=self.user)

    def tearDown(self):
        self.client.logout()

    def test_jwt_in_cookies_when_logged_in(self):
        """
        Test the request from login retrieve cookies for jwt authentication
        """
        data = {"email": self.userProfile.user.email, "password": "useruser"}

        response = self.client.post(reverse("login"), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.client.cookies.get("JWT-refresh"))
        self.assertTrue(response.client.cookies.get("JWT-access"))

    def test_jwt_not_in_cookies_when_logged_in_with_wrong_pw(self):
        """
        Test the request from login retrieve cookies for jwt authentication
        """
        data = {"email": self.userProfile.user.email, "password": "badPassword"}
        response = self.client.post(reverse("login"), data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.client.cookies.get("JWT-refresh"))
        self.assertFalse(response.client.cookies.get("JWT-access"))


class UnicornDetailTests(APITestCase):
    def setUp(self):
        self.user = SimpleUserFactory()
        self.userProfile = SimpleUserProfileFactory(user=self.user)
        self.unicorn_maxime = BaseUnicornFactory(name="Maxime")
        self.url = reverse("unicorn_detail", kwargs={"pk": self.unicorn_maxime.id})

    def tearDown(self):
        self.client.logout()

    def test_get_unicorn_detail_without_authentification(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_unicorn_detail_with_authentification(self):
        self.client.login(email=self.userProfile.user.email, password="useruser")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, model_to_dict(self.unicorn_maxime))


class UnicornListTests(APITestCase):
    def setUp(self):
        self.unicorn_nicola = BaseUnicornFactory(name="Nicola")
        self.unicorn_maxime = BaseUnicornFactory(name="Maxime")
        self.unicorn_florent = BaseUnicornFactory(name="Florent")
        self.url = reverse("unicorns_list")

    def test_get_all_unicorns(self):
        """
        Ensure the views return all created unicorn
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Unicorn.objects.count(), Unicorn.objects.count())

    def test_add_unicorn(self):
        """
        Ensure we can create a new unicorn object.
        """
        data = {"name": "Thomas", "model": "Model S", "price": 3.9}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Unicorn.objects.filter(name="Thomas").exists())
        self.assertEqual(Unicorn.objects.count(), Unicorn.objects.count())


class UsersListView(APITestCase):
    def setUp(self):
        self.adminUser = AdminUserFactory()
        self.adminProfile = AdminUserProfileFactory(user=self.adminUser)
        self.user = SimpleUserFactory()
        self.userProfile = SimpleUserProfileFactory(user=self.user)

    def tearDown(self):
        self.client.logout()

    def test_get_all_users_as_admin(self):
        url = reverse("user-list")
        self.client.login(
            email=self.adminProfile.user.email, password="adminadmin")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], User.objects.count())

    def test_cant_get_all_users_as_user(self):
        url = reverse("user-list")
        self.client.login(
            email=self.userProfile.user.email, password="useruser")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_user_with_valid_data(self):
        url = reverse("user-list")
        data = {
            "email": "test@test.com",
            "password": "testtest",
            "profile": {
                "address": "2 rue de la boisson"
            }
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="test@test.com").exists())

    def test_cant_add_user_with_missing_value(self):
        url = reverse("user-list")
        data = {
            "email": "badtest@badtest.com",
            "password": "testtest",
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(email=data["email"]).exists())

    def test_user_can_access_his_own_profile(self):
        url = reverse("user-detail", kwargs={"pk": self.userProfile.user.id})
        self.client.login(
            email=self.userProfile.user.email, password="useruser")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.userProfile.user.email)

    def test_user_can_edit_his_own_profile(self):
        url = reverse("user-detail", kwargs={"pk": self.userProfile.user.id})
        data = {
            "email": self.userProfile.user.email,
            "first_name": "Gerard",
            "last_name": "Menvuca",
            "password": "useruser",
            "profile": {
                "address": self.userProfile.address
            }
        }
        self.client.login(
            email=self.userProfile.user.email, password="useruser")
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.data["first_name"])
        self.assertEqual(response.data["last_name"], self.data["last_name"])

    def test_user_cant_edit_other_user_profile(self):
        pass

    def test_admin_can_edit_all_user_profile(self):
        pass

    def test_user_cant_access_other_user_profile(self):
        url = reverse("user-detail", kwargs={"pk": self.adminProfile.user.id})
        self.client.login(
            email=self.userProfile.user.email, password="useruser")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_access_other_user_profile(self):
        url = reverse("user-detail", kwargs={"pk": self.userProfile.user.id})
        self.client.login(
            email=self.adminProfile.user.email, password="adminadmin")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.userProfile.user.email)
