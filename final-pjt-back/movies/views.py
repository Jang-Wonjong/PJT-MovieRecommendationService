from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def review_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        # reviews = Review.objects.all()
        reviews = Review.objects.filter(movie_id=movie_pk).order_by('-pk')
        # paginator = Paginator(reviews, 5)
        # page_number = request.GET.get('page_num')
        # reviews = paginator.get_page(page_number)
        serializer = ReviewSerializer(reviews, many=True)
        # data.append({'possible_page': paginator.num_pages})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_update_or_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_list_or_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        # reviews = Review.objects.all()
        comments = Comment.objects.filter(review_id=review_pk).order_by('-pk')
        # paginator = Paginator(reviews, 5)
        # page_number = request.GET.get('page_num')
        # reviews = paginator.get_page(page_number)
        serializer = CommentSerializer(comments, many=True)
        # data.append({'possible_page': paginator.num_pages})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def comment_update_or_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def my_movies(request):
    my_movies = MyMovie.objects.filter(user_id=request.user.pk).order_by('-pk')
    # paginator = Paginator(photo_tickets, 12)
    # page_num = request.GET.get('page_num')
    # photo_tickets = paginator.get_page(page_num)
    serializer = MyMovieSerializer(my_movies, many=True)
    # serializer.data.append({'possible_page': paginator.num_pages})
    return Response(serializer.data)


@api_view(['POST', 'DELETE'])
@permission_classes([AllowAny])
def my_movie(request, movie_pk):
    # if request.method == 'GET':
    #     my_movie = MyMovie.objects.filter(user_id=request.user.pk, movie_id=movie_pk).first()
    #     serializer = MyMovieSerializer(my_movie)
    #     return Response(serializer.data)

    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MyMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie, title=movie.title, poster_path=movie.poster_path)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        my_movie = MyMovie.objects.filter(user_id=request.user.pk, movie_id=movie_pk).first()
        my_movie.delete()
        data = {
            'delete' : '포토티켓이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


    # my_movies = PhotoTicket.objects.filter(user__pk=request.user.pk).order_by('-pk')
    # # paginator = Paginator(photo_tickets, 12)
    # # page_num = request.GET.get('page_num')
    # # photo_tickets = paginator.get_page(page_num)
    # serializer = PhotoTicketSerializer(photo_tickets, many=True)
    # data = serializer.data
    # data.append({'possible_page': paginator.num_pages})
    # return Response(data)

    # elif request.method == 'POST':
    #     movie = get_object_or_404(Movie, pk=movie_pk)
    #     serializer = PhotoTicketSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user, movie=movie, poster_path=movie.poster_path, title=movie.title)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)