from django.contrib import admin

from .models import (Book, Author, Publisher,
                     Rating, Stock)

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Rating)
admin.site.register(Stock)
