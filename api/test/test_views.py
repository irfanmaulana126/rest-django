
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Posts
from ..serializers import PostsSerializer

client = Client()

class GetAllPostsTest(TestCase):    
    def setUp(self):
        Posts.objects.create(
            title="Hello World Python",
            author="Irfan Maulana",
            content="All about beginer base code python"
        )
        Posts.objects.create(
            title="Basic Python",
            author="Rizwan Akhir",
            content="Base code python"
        )

    def test_get_all_posts(self):
        response = client.get(reverse('get_post_posts'))

        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePostsTest(TestCase):
    def setUp(self):
        self.irfan = Posts.objects.create(
            title="Hello World Python",
            author="Irfan Maulana",
            content="All about beginer base code python"
        )
        self.rizwan = Posts.objects.create(
            title="Basic Python",
            author="Rizwan Akhir",
            content="Base code python"
        )
    
    def test_get_valid_single_posts(self):
        response = client.get(
            reverse('get_delete_put_posts', kwargs={'pk': self.irfan.pk}))
        posts = Posts.objects.get(pk=self.irfan.pk)
        serializer = PostsSerializer(posts)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_posts(self):
        response = client.get(
            reverse('get_delete_put_posts', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewPostsTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'title':'Basic Python',
            'author':'Rizwan Akhir',
            'content':'Base code python'
        }

        self.invalid_payload = {
            'title':'',
            'author':'Rizwan Akhir',
            'content':'Base code python'
        }

    def test_create_valid_posts(self):
        response = client.post(
            reverse('get_post_posts'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_posts(self):
        response = client.post(
            reverse('get_post_posts'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePostsTest(TestCase):
    def setUp(self):        
        self.irfan = Posts.objects.create(
            title="Hello World Python",
            author="Irfan Maulana",
            content="All about beginer base code python"
        )
        self.rizwan = Posts.objects.create(
            title="Basic Python",
            author="Rizwan Akhir",
            content="Base code python"
        )

        self.valid_payload = {
            'title':'Basic Python',
            'author':'Rizwan Akhir',
            'content':'Base code python'
        }

        self.invalid_payload = {
            'title':'',
            'author':'Rizwan Akhir',
            'content':'Base code python'
        }

    def test_valid_update_posts(self):
        response = client.put(
            reverse('get_delete_put_posts', kwargs={'pk': self.rizwan.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_posts(self):
        response = client.put(
            reverse('get_delete_put_posts', kwargs={'pk': self.rizwan.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePostsTest(TestCase):

    def setUp(self):
        self.irfan = Posts.objects.create(
            title="Hello World Python",
            author="Irfan Maulana",
            content="All about beginer base code python"
        )
        self.rizwan = Posts.objects.create(
            title="Basic Python",
            author="Rizwan Akhir",
            content="Base code python"
        )

    def test_valid_delete_post(self):
        response = client.delete(
            reverse('get_delete_put_posts', kwargs={'pk': self.irfan.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_post(self):
        response = client.delete(
            reverse('get_delete_put_posts', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)