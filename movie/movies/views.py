from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import  Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer


class MoviePageNumberPagination(PageNumberPagination):
    page_size = 5

class ActorPageNumberPagination(PageNumberPagination):
    page_size = 7

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         data = request.data
#         serializer = MovieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MovieList(APIView):
#     def get(self, request):
#         movies=Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePageNumberPagination



# @api_view(['GET', 'POST'])
# def actor_list(request):
#     if request.method == 'GET':
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         data = request.data
#         serializer = ActorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class ActorList(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = ActorPageNumberPagination



# @api_view(['GET','PATCH','DELETE'])
# def actor_detail(request, pk):
#     actor = get_object_or_404(Actor, pk=pk)
#     if request.method == 'GET':
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class ActorDetail(APIView):
#     def get_object(self, request, pk):
#         actor = get_object_or_404(Actor, pk=pk)
#         return actor
#
#     def get(self, request, pk):
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor, many=True)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         actor = self.get_object(pk)
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer





# @api_view(['GET', 'PATCH', 'DELETE'])
# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class MovieDetail(APIView):
#     def get_objects(self, pk):
#         movie = get_object_or_404(Movie, pk=pk)
#         return movie
#     def get(self, request, pk):
#         movie = self.get_objects(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         movie = self.get_objects(pk)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request, pk):
#         movie = self.get_objects(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer





# @api_view(['GET', 'POST'])
# def review_list(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     if request.method == 'GET':
#         reviews = Review.objects.filter(movie=movie)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)




# Create your views here.
