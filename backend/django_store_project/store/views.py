from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Game, Genre
from .permissions import (StaffPostGamePermission,
                          StaffPutDeleteGamePermission, isAdminOrReadOnly)
from .serializers import GameSerializer, GenreSerializer


class GenreAPIView(generics.ListCreateAPIView):
    # only superuser is allowed to use this APIView
    permission_classes = [isAdminOrReadOnly]
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def delete(self, request):
        # DELETE ALL GENRES !! For development purposes only !
        Genre.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameAPIView(generics.ListCreateAPIView):
    # Anybody is allowed to use GET method
    # Only staff is allowed to use POST method
    # Only superuser is allowed to use DELETE method (for development and purposes only!!!)
    permission_classes = [StaffPostGamePermission]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('genre',)
    search_fields = ('name', 'description')

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    # DELETE ALL GAMES !! For test purposes only. TODO: limit access to this method for admin only ASAP
    def delete(self, request):
        Game.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Anybody is allowed to use GET method
    # Only staff is allowed to utilize POST, PUT and DELETE
    permission_classes = [StaffPutDeleteGamePermission]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        return self.destroy(request)


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
