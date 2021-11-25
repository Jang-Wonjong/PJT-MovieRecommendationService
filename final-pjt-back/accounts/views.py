from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

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


@api_view(['GET'])
@permission_classes([AllowAny])
def login_info(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def profile(request, user_pk):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        image = request.data.get('image')
        if request.user.nickname != request.data.get('nickname') and get_user_model().objects.filter(nickname=request.data.get('nickname')).exists():
            return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProfileSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(image=image)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user = request.user.pk
        request.user.delete()
        return Response({ 'delete': f'{user}번 회원이 탈퇴했습니다.' }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([AllowAny])
def follow(request, you_pk):
    # me = get_user_model().objects.get(id=me_pk)
    # you = get_user_model().objects.get(id=you_pk)
    # if me != you:
    #     if you in me.followings.all():
    #         me.followings.remove(you)
    #     else:
    #         me.followings.add(you)
    me = request.user
    you = get_object_or_404(get_user_model(), pk=you_pk)
    
    if me != you:
 
        if you.followers.filter(pk=me.pk).exists():
        # 언팔로우
            you.followers.remove(me)
        else:
        # 팔로우
            you.followers.add(me)
    
        return Response("follow success") 


@api_view(['GET'])
def followings(request, me_pk):
    user = get_user_model().objects.get(pk=me_pk)
    follows = user.followings.all().order_by('id')
    data = []
    for follow in follows:
        box={}
        box['id'] = follow.id
        box['username'] = follow.username
        box['nickname'] = follow.nickname
        # if follow.userImage == 'undefined':
        #     box['img'] = None
        # else:
        #     box['img'] = str(follow.userImage)
        data.append(box)
    return Response(data)


@api_view(['GET'])
def followers(requets, me_pk):
    me = get_user_model().objects.get(pk=me_pk)
    data = []
    print(me.username)
    user = get_user_model().objects.all().order_by('id')
    for i in user:
        if me.username != i.username:
            box = {}
            flag = 0
            follower = i.followings.all()
            for j in follower:
                if j.username == me.username:
                    flag = 1
                    box['id'] = i.id
                    box['username'] = i.username
                    box['nickname'] = i.nickname
                    # if i.username == 'undefined':
                    #     box['img'] = None
                    # else:
                    #     box['img'] = str(i.userImage)
                    break
            if flag:
                data.append(box)
    return Response(data)