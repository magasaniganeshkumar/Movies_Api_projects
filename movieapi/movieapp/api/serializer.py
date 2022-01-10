from rest_framework import serializers
from movieapp.models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.movie_name = validated_data.get('movie_name', instance.movie_name)
        instance.language = validated_data.get('language', instance.language)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance