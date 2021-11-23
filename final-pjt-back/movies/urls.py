from django.urls import path
from . import views


urlpatterns = [
    # movie
    path('list/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),

    # review
    path('<int:movie_pk>/review/', views.review_list_or_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_update_or_delete),
    
    # comment
    path('review/<int:review_pk>/comment/', views.comment_list_or_create),
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_update_or_delete),
    
    # my movie add
    path('user-movies/<int:user_pk>/', views.user_movies),
    path('<int:movie_pk>/user-movies/', views.user_movies_create_or_delete),

    path('recommend-user/', views.recommend_user),
]