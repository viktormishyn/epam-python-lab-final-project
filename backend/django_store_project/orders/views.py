from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Cart
from .permissions import isAdminOrReadOnly  # TODO
from rest_framework.permissions import IsAdminUser
from .serializers import CartSerializer


class ListCart(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
