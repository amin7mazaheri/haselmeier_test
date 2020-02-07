from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from bookshop_base.models import Book, Author, Rating, Stock, Publisher
from bookshop_base.serializers import (StockSerializer,
                                       BookSerializer,
                                       RatingSerializer)



BOOK_URL = '/api/book/'


class BookApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'amin@gmail.com',
            'amin')
        self.client.force_authenticate(self.user)
        self.publisher1 = Publisher.objects.create(name='hekmataneh')
        self.publisher2 = Publisher.objects.create(name='haselmeire')
        self.author1 = Author.objects.create(
            first_name='Hesam', last_name='Mahboub')
        self.author2 = Author.objects.create(
            first_name='Ali', last_name='Ghaedi')

    def test_retrieve_book_list(self):
        Book.objects.create(author=self.author1, name='Potato',
                            price=10000, publisher=self.publisher1)

        res = self.client.get(BOOK_URL + '1/')
        book = Book.objects.get(id=1)
        serializer = BookSerializer(book)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_create_book_successful(self):
        payload = {'name': 'Cabbage', 'price': 88888,
                   'author': 1, 'publisher': 1}
        self.client.post(BOOK_URL, payload)
        exists = Book.objects.filter(name=payload['name'],).exists()
        self.assertTrue(exists)


RATING_URL = '/api/rating/'


class RatingApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'Ali@gmail.com',
            'Ali')
        self.client.force_authenticate(self.user)
        self.author = Author.objects.create(
            first_name='Hesam', last_name='Mahboub')
        self.publisher = Publisher.objects.create(name='hekmataneh')
        self.book = Book.objects.create(author=self.author, name='Potato',
                                        price=1234, publisher=self.publisher)

    def test_retrieve_rating_list(self):
        Rating.objects.create(user=self.user, book=self.book, rating=2)

        res = self.client.get(RATING_URL + '1/')
        rating = Rating.objects.get(id=1)
        serializer = RatingSerializer(rating)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)


STOCK_URL = '/api/stock/'


class StockApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'Ali@gmail.com',
            'Ali')
        self.client.force_authenticate(self.user)
        self.author = Author.objects.create(
            first_name='Hesam', last_name='Mahboub')
        self.publisher = Publisher.objects.create(name='hekmataneh')
        self.book = Book.objects.create(author=self.author, name='Potato',
                                        price=1234, publisher=self.publisher)

    def test_retrieve_stock_item(self):
        Stock.objects.create(quantity=120, book=self.book, in_stock=True)

        res = self.client.get(STOCK_URL + '1/')
        rating = Stock.objects.get(id=1)
        serializer = StockSerializer(rating)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)
