from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartListCreateAPIView(generics.ListCreateAPIView):
    """
    GET: List all carts (admin view)
    POST: Create a new cart
    """
    queryset = Cart.objects.all().prefetch_related('cart_items__product')
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific cart
    PUT/PATCH: Update a cart
    DELETE: Delete a cart
    """
    queryset = Cart.objects.all().prefetch_related('cart_items__product')
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class UserCartAPIView(generics.RetrieveAPIView):
    """
    GET: Retrieve the authenticated user's cart
    """
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart

class CartItemCreateAPIView(generics.CreateAPIView):
    """
    POST: Add an item to the cart
    """
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = self.get_cart()
        serializer.save(cart=cart)

    def get_cart(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart

class CartItemUpdateAPIView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update a cart item
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

class CartItemDeleteAPIView(generics.DestroyAPIView):
    """
    DELETE: Remove a cart item
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
