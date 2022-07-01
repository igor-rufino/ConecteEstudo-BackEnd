from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
import json
from datetime import datetime


class NewUserTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        timestamp = datetime.now()
        super().setUpClass()
        cls.client = APIClient()
        cls.new_user_dict = json.dumps(
            {
                "userName": "name - " + str(timestamp),
                "email": "email - " + str(timestamp),
                "password": "test",
                "phone": "12341234",
                "birthdate": "2022-01-01",
                "profileType": 1,
                "createdAt": "2022-01-01",
                "updatedAt": "2022-01-01",
            }
        )

    def test_if_new_user_can_be_created(self):
        response = self.client.post(
            path="http://127.0.0.1:8000/user",
            data=self.new_user_dict,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(path="http://127.0.0.1:8000/user")
        users_created = len(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(users_created, 1)
