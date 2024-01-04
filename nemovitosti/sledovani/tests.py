from django.test import TestCase
from django.urls import reverse

class PageTestCase(TestCase):
    def test_display_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_display_registration(self):
        response = self.client.get(reverse("registration"))
        self.assertEqual(response.status_code, 200)

    def test_create_registration(self):
        password = "12345Kombajn"
        response = self.client.post(
        reverse("registration"))
        (
            "username" = "franta"
            "password1" = password,
            "password2" = password,

        ),

        self.assertRedirects(response, reverse("login"))
        self.assertEqual(response.status_code, 302)




