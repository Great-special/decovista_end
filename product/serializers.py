from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Products, Review, Category


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"



class ProductsSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all(), write_only=True
    )
    
    class Meta:
        model = Products
        fields = [
            'id',
            'designer',
            'product_name',
            'categories',
            'category_ids',
            'brand',
            'price',
            'description',
            'image',
            'image_2',
            'image_3',
        ]
    
    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids', [])
        product = Products.objects.create(**validated_data)
        product.categories.set(category_ids)
        return product
    
    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids', [])
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.description = validated_data.get('description', instance.description)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.image_2 = validated_data.get('image_2', instance.image_2)
        instance.image_3 = validated_data.get('image_3', instance.image_3)
        instance.save()
        if category_ids:
            instance.categories.set(category_ids)
        return instance


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"