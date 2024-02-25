from rest_framework.serializers import ValidationError


class PriceValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        price = value.get('price')
        print(price)
        if price == 0.00:
            raise ValidationError('Не указана цена товара')
        if price <= 0:
            raise ValidationError('Цена товара должна быть больше 0')
