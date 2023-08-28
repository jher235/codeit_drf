from rest_framework import serializers
from .models import Movie, Actor, Review
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     opening_date = serializers.DateField()
#     running_time = serializers.IntegerField()
#     overview = serializers.CharField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.opening_date = validate_data.get('opening_date', instance.opening_date)
#         instance.running_time = validate_data.get('running_time', instance.running_time)
#         instance.overview = validate_data.get('overview', instance.overview)
#         instance.save()
#         return instance



# class MVSerializer(serializers.ModelSerializer):
#



def overview_validator(value):
    if value > 300:
        raise ValidationError('소개 문구는 최대 300자 이하로 작성해야 합니다.')
    elif value < 10:
        raise ValidationError('소개 문구는 최대 10자 이상으로 작성해야 합니다.')
    return value

class MovieSerializer(serializers.ModelSerializer):
    # overview = serializers.CharField(validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=300)])
    # overview = serializers.CharField(validators=[overview_validator])
    # def validate_overview(self, value):
    #     if 10 <= len(value) and len(value)<=300:
    #         return value
    #     raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
    def validate(self, attrs):
        if 10>len(attrs['overview']) or len(attrs['overview'])>300:
            raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
        if len(attrs['name']) > 50:
            raise ValidationError('영화 이름은 50자 이하로 작성해주세요.')
        return attrs




    # name = serializers.CharField(validators=[UniqueValidator(
    #     queryset=Movie.objects.all(),
    #     message='이미 존재하는 영화 이름입니다.',
    # )])

    # movie_reviews = serializers.PrimaryKeyRelatedField(source='reviews', many=True, read_only=True)
    # reviews = serializers.StringRelatedField(many=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    actors = serializers.StringRelatedField(many=True, read_only=True)
    # MV_actor = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'name', 'reviews', 'actors', 'opening_date', 'running_time', 'overview']
        read_only_fields = ['reviews', 'actors']
        validators = [
            UniqueTogetherValidator(
                queryset=Movie.objects.all(),
                fields=['name', 'overview'],
            )
        ]


class ReviewSerializer(serializers.ModelSerializer):
    # movie = serializers.StringRelatedField()
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
        extra_kwargs = {
            'movie': {'read_only': True}
        }




# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True) #Serializer 클래스의 id 필드는 조회할 때만 사용되고 생성할 때는 사용되지 않게 작성해 주세요.
#     name = serializers.CharField(max_length=10)
#     gender = serializers.CharField(max_length=1)
#     birth_date = serializers.DateField()
#
#     def create(self,validate_data):
#         return Actor.objects.create(**validate_data)
#
#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.gender = validate_data.get('gender', instance.gender)
#         instance.birth_date = validate_data.get('birth_date',instance.birth_date)
#         instance.save()
#         return instance

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(read_only=True, many=True)
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date', 'movies']





