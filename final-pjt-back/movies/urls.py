from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),

    path('<int:movie_pk>/review/', views.review_list_or_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_update_or_delete),
]