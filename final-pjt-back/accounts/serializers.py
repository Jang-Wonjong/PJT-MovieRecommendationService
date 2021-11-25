from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'nickname', 'image')   # followings 넣으면 가입 안됨
        # fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'image')
        # fields = '__all__'