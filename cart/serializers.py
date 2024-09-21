from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)  # Nested serializer for cart items

    class Meta:
        model = Cart
        fields = ['id', 'products', 'cart_items', 'total_amount']

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)
        for item_data in cart_items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart

    def update(self, instance, validated_data):
        cart_items_data = validated_data.pop('cart_items', [])
        instance.products.set(validated_data.get('products', instance.products))

        # Update or create cart items
        for item_data in cart_items_data:
            item_id = item_data.get('id')
            if item_id:
                # Update existing cart item
                item = CartItem.objects.get(id=item_id, cart=instance)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            else:
                # Create new cart item
                CartItem.objects.create(cart=instance, **item_data)

        instance.save()
        return instance
