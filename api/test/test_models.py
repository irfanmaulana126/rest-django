from turtle import title
from django.test import TestCase
from ..models import Posts

class PostsTest(TestCase):
    
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