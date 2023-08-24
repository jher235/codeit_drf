from rest_framework import serializers
from .models import Movie, Actor


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.opening_date = validate_data.get('opening_date', instance.opening_date)
        instance.running_time = validate_data.get('running_time', instance.running_time)
        instance.overview = validate_data.get('overview', instance.overview)
        instance.save()
        return instance

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True) #Serializer 클래스의 id 필드는 조회할 때만 사용되고 생성할 때는 사용되지 않게 작성해 주세요.
    name = serializers.CharField(max_length=10)
    gender = serializers.CharField(max_length=1)
    birth_date = serializers.DateField()

    def create(self,validate_data):
        return Actor.objects.create(**validate_data)