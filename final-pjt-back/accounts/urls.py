from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('signup/', views.signup),
    path('<username>/', views.login_info),              # 로그인 시 Vue에 로그인 정보 저장
    path('<int:user_pk>/profile/', views.profile),      # 프로필 가져오기
    path('follow/<int:you_pk>/', views.follow),         # 팔로우 하기
    path('followings/<int:me_pk>/', views.followings),  # 팔로잉 보기
    path('followers/<int:me_pk>/', views.followers),    # 팔로워 보기
]