from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from .models import Book, Rating, Stock
from .serializers import (StockSerializer,
                          BookSerializer,
                          RatingSerializer)


class BookViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    """
    The following endpoints are fully provided by mixins:
    * Retrieve view
    * Create view
    * Edite view
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RatingViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    """
    The following endpoints are fully provided by mixins for Rating:
    * Retrieve view
    * Create view
    * Delete
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class StockViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin, 
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    """
    The following endpoints are fully provided by mixins for Stock:
    * Retrieve view
    * Create view
    * Delete
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated,)
