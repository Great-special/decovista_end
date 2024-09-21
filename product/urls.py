from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductsListCreateAPIView.as_view(), name='products-list-create'),
    path('product/<int:pk>/', ProductsDetailAPIView.as_view(), name='products-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories-list-create'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    
]
