from rest_framework import serializers
from .models import Movie, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'rank',)


# class MovieSerializer(serializers.ModelSerializer):
#     review_set = ReviewSerializer(many=True, read_only=True)

#     class Meta:
#         model = Movie
#         fields = (
#             'id',
#             'adult',
#             'backdrop_path',
#             'genre_ids',
#             'tmdb_id',
#             'original_language',
#             'original_title',
#             'overview',
#             'popularity',
#             'poster_path',
#             'release_date',
#             'title',
#             'video',
#             'vote_average',
#             'vote_count',
#             'review_set',
#         )

# class ReviewSerializer(serializers.ModelSerializer):
#     class MovieSerializer(serializers.ModelSerializer):
#     # 역참조 매니저 명과 같게 만들어야함
        
#         class Meta:
#             model = Movie
#             fields = '__all__'
             
#     # movies = MovieSerializer(read_only=True)
#     class Meta:
#         model = Review
#         fields = ('title', 'content', 'rank')
#         # read_only_fields = ('movies', )