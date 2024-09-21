from django.db import models
from product.models import Products
from users.models import User
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True)
    # Remove the 'products' field as it's managed through 'cart_items'

    def total_amount(self):
        total = sum(item.amount() for item in self.cart_items.all())
        return total

    def __str__(self):
        return f"Cart ID: {self.id} for {self.user.username}"

class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()

    def amount(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Cart"
    
    
