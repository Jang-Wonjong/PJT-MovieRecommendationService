from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers import MovieSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'nickname',)


class UserProfileSerializer(serializers.ModelSerializer):
    my_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'nickname', 'my_movies')