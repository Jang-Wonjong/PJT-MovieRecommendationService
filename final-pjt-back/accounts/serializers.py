from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    # followers = serializers.

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'nickname', 'followings')
        # fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('nickname',)
        # fields = '__all__'