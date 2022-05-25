from dataclasses import field
from pyexpat import model
from .models import Posts
from rest_framework import serializers

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'