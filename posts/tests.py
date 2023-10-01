import json
from django.urls import reverse
from django.test import TestCase

class PostCreateTestCase(TestCase):
    def test_create_post(self):
        url = reverse('posts:create')
        data = {
            "id": "114034c2-6076-11ee-8c99-0242ac120001",
            "content": "this is yet another post"
        }
        data_json = json.dumps(data)

        response = self.client.post(
            url,
            data=data_json,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Successfully created a new post')

    def test_create_post_invalid_data(self):
        url = reverse('posts:create')
        data = {
            "id": "invalid id",
            "content": "this is yet another post"
        }
        data_json = json.dumps(data)

        response = self.client.post(
            url,
            data=data_json,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 500)
