from store.models import Game
from store.serializers import GameSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins


class GameAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

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
