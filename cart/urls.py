from django.urls import path
from .views import (
    CartListCreateAPIView,
    CartRetrieveUpdateDestroyAPIView,
    UserCartAPIView,
    CartItemCreateAPIView,
    CartItemUpdateAPIView,
    CartItemDeleteAPIView,
)

urlpatterns = [
    path('', CartListCreateAPIView.as_view(), name='cart-list-create'),
    path('<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart-detail'),
    path('user/cart/', UserCartAPIView.as_view(), name='user-cart'),
    path('cart-items/', CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('cart-items/<int:pk>/', CartItemUpdateAPIView.as_view(), name='cartitem-update'),
    path('cart-items/<int:pk>/delete/', CartItemDeleteAPIView.as_view(), name='cartitem-delete'),
]
