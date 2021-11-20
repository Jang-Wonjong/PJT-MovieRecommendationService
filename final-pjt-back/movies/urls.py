from django.urls import path
from . import views


urlpatterns = [
    # movie
    path('list/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),

    # review
    path('<int:movie_pk>/review/', views.review_list_or_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_update_or_delete),
    # my list
    path('<int:movie_pk>/my-list/', views.my_list),

    # comment
    path('review/<int:review_pk>/comment/', views.comment_list_or_create),
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_update_or_delete),

]