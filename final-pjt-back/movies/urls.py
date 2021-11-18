from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),

    path('<int:movie_pk>/review/', views.review_list_or_create),
]