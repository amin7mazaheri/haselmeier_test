from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bookshop_base import views

api_router = DefaultRouter()
api_router.register(r'book', views.BookViewSet, 'book')
api_router.register(r'rating', views.RatingViewSet, 'rating')
api_router.register(r'stock', views.StockViewSet, 'stock')

urlpatterns = [
    path('api/', include((api_router.urls, 'api_router'), namespace='api'))
]
