from django.shortcuts import render
from rest_framework.views import APIView
from movieapp.models import Movies
from movieapp.api.serializer import MoviesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404


class MovieApi(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('pk'):
            pk = kwargs.get('pk')
            saved_movie = get_object_or_404(Movies.objects.all(), pk=pk)
            serializer = MoviesSerializer(saved_movie)
            return Response({"Movie": serializer.data})

        movies = Movies.objects.all()
        movies = MoviesSerializer(movies, many=True)
        return Response({'Movies': movies.data})
        # return HttpResponse({'Movies': movies.data})

    def post(self, request):

        serializer = MoviesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        movie = get_object_or_404(Movies.objects.all(), pk=pk)
        serializer = MoviesSerializer(instance=movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            movie_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(movie_saved.movie_name)})

    def delete(self, request, pk):
        # Get object with this pk
        movie = get_object_or_404(Movies.objects.all(), pk=pk)
        movie.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)

# Create your views here.
