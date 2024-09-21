from django.urls import path
from .views import (
    CartDetailView,
   CartItemDetailView,
   CartListCreateView,
   CartItemListCreateView
)

urlpatterns = [
    path('', CartListCreateView.as_view(), name='cart-list-create'),
    path('<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),
]