from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartDetailView(generics.RetrieveAPIView):
    """View to get the cart for the authenticated user."""
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        return self.request.user.cart

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class CartItemCreateView(generics.CreateAPIView):
    """View to add items to the cart."""
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemUpdateView(generics.UpdateAPIView):
    """View to update an item in the cart."""
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def patch(self, request, *args, **kwargs):
        cart_item = self.get_object()
        serializer = self.get_serializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDeleteView(generics.DestroyAPIView):
    """View to remove an item from the cart."""
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def delete(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

