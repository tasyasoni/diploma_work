from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from pricingapp.models import Product
from pricingapp.permissions import IsSeller
from pricingapp.serializers import ProductSerializer


class PriceCreateView(generics.CreateAPIView):
    """
    Сериализатор для создания нового продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]
