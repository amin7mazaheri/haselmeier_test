from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    '''model for authers
    '''
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Publisher(models.Model):
    '''model for publisher
    '''
    name = models.CharField(max_length=60)
    address = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    '''model for book
    '''
    name = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    '''this class used for holding review of
        book by users
    '''
    rate = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=rate)

    def __str__(self):
        return self.book.name + "/ " +str(self.rating)


class Stock(models.Model):
    '''Stock model for book '''
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.quantity > 0:
            self.in_stock = True
            super(Stock, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.quantity) + " " +self.book.name
