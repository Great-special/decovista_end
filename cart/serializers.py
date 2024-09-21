from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'cart_items', 'total_amount']
        read_only_fields = ['id', 'total_amount']

    # Cart of already existing user or create new
    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items', [])
        user = self.context['request'].user
        cart, created = Cart.objects.get_or_create(user=user)
        if not created:
            raise serializers.ValidationError("Cart already exists for this user.")
        for item_data in cart_items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart

    def update(self, instance, validated_data):
        cart_items_data = validated_data.pop('cart_items', [])
        # Update cart items
        for item_data in cart_items_data:
            item_id = item_data.get('id', None)
            if item_id:
                try:
                    cart_item = CartItem.objects.get(id=item_id, cart=instance)
                    cart_item.quantity = item_data.get('quantity', cart_item.quantity)
                    cart_item.product = item_data.get('product', cart_item.product)
                    cart_item.save()
                except CartItem.DoesNotExist:
                    raise serializers.ValidationError(f"CartItem with id {item_id} does not exist in this cart.")
            else:
                # Create new cart item
                CartItem.objects.create(cart=instance, **item_data)
        return instance
