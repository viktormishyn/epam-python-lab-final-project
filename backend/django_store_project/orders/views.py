from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Order
from .permissions import isAdminOrReadOnly  # TODO
from rest_framework.permissions import IsAdminUser
from .serializers import OrderSerializer


class ListOrder(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
