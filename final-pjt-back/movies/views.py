from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer
from .models import Movie, Review


# Create your views here.
@api_view(['GET'])
# @permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
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