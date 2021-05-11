from store.models import Game, Genre
from store.serializers import GameSerializer, GenreSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class GenreAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def delete(self, request):
        # DELETE ALL GENRES !! For test purposes only. TODO: limit access to this method for admin only
        Genre.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
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


class GameDetailAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        return self.destroy(request)
