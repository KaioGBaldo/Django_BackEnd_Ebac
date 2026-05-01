import asyncio
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product, Category, Post, Order
from .serializers import ProductSerializer, CategorySerializer, PostSerializer, OrderSerializer

async def async_view_example(request):
    print("Iniciando task assíncrona...")
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(f"Segundos passados: {i}")
    return HttpResponse("Visualização Assíncrona Completa!")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
