from rest_framework import serializers

from .models import Book, Rating, Stock


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'price')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', 'date')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('in_stock', 'quantity')
