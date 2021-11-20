from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, UserProfileSerializer


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if get_user_model().objects.filter(username=request.data.get('username')).exists():
        return Response({'error': '일치하는 아이디가 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if get_user_model().objects.filter(nickname=request.data.get('nickname')).exists():
        return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()

        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def profile(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # image = request.data.get('image')
        if request.user.nickname != request.data.get('nickname') and get_user_model().objects.filter(nickname=request.data.get('nickname')).exists():
            return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProfileSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user_pk = request.user.pk
        request.user.delete()
        return Response({ 'delete': f'{user_pk}번 회원이 탈퇴했습니다.' }, status=status.HTTP_204_NO_CONTENT)
