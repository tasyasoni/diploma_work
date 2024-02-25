from rest_framework import serializers
from pricingapp.models import Product
from pricingapp.validators import PriceValidator


class ProductSerializer(serializers.ModelSerializer):
    """
       Сериализатор для модели Product.
       Для преобразования объектов Product в формат JSON и обратно.
       Он определяет, какие поля модели должны быть сериализованы.
       Также добавляет динамическое поле total_price в сериалайзер.

    """
    total_price = serializers.SerializerMethodField(read_only=True)

    def get_total_price(self, instance):
        return instance.total_price

    class Meta:
        model = Product
        fields = ('name', 'price', 'total_price')
        validators = [
            PriceValidator(field='price'),
        ]
