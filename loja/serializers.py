from rest_framework import serializers
from .models import Product, Category, Post, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True, slug_field='title', queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'category']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
