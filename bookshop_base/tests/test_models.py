from django.test import TestCase
from django.contrib.auth import get_user_model

from bookshop_base.models import Book, Author, Rating, Stock, Publisher


class BookTestCase(TestCase):
    '''test Book model'''

    def setUp(self):
        author = Author.objects.create(first_name="Vahid", last_name="Mahboub")
        publisher = Publisher.objects.create(name='hekmataneh')
        Book.objects.create(name="cat and mouse", author=author,
                            publisher=publisher, price=100.12)

    def test_book(self):

        book = Book.objects.get(name="cat and mouse")
        self.assertEqual(book.author.first_name, "Vahid")
        self.assertEqual(book.author.last_name, "Mahboub")

    def test_book_publisher(self):
        '''Test model Book for publisher'''
        book = Book.objects.get(name="cat and mouse")
        self.assertEqual(book.publisher.name, "hekmataneh")

    def test_book_price(self):
        '''Test model Book for publisher'''
        book = Book.objects.get(name="cat and mouse")
        self.assertNotEqual(book.price, 100)


class StockTestCase(TestCase):
    '''Test Stock model'''

    def setUp(self):
        author = Author.objects.create(first_name="Vahid", last_name="Mahboub")
        publisher = Publisher.objects.create(name='hekmataneh')
        book = Book.objects.create(name="cat and mouse", author=author,
                                   publisher=publisher, price=100.12)
        Stock.objects.create(book=book, in_stock=True, quantity=120)

    def test_stock_quantity(self):
        stock1 = Stock.objects.get(id=1)
        self.assertEqual(stock1.quantity, 120)

    def test_stock_in_stock(self):
        stock1 = Stock.objects.get(id=1)
        self.assertEqual(stock1.in_stock, True)


class RatingTestCase(TestCase):
    '''Test Rating model'''

    def setUp(self):
        author = Author.objects.create(first_name="Vahid", last_name="Mahboub")
        publisher = Publisher.objects.create(name='hekmataneh')
        book = Book.objects.create(name="cat and mouse", author=author,
                                   publisher=publisher, price=100.12)
        self.user = get_user_model().objects.create_user(
            'admin@gmail.com',
            'amin')
        Rating.objects.create(book=book, rating=5, user=self.user)
        Rating.objects.create(book=book, rating=3, user=self.user)

    def test_rating_book(self):
        rating = Rating.objects.get(id=1)
        self.assertEqual(rating.book.name, "cat and mouse")

    def test_rating_user(self):
        rating = Rating.objects.get(id=1)
        self.assertEqual(rating.user.username, "admin@gmail.com")

    def test_rating_rate(self):
        rating1 = Rating.objects.get(id=1)
        rating2 = Rating.objects.get(id=2)
        self.assertEqual(rating1.rating, 5)
        self.assertNotEqual(rating2.rating, 5)
