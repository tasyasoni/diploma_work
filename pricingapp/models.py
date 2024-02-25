from django.db import models


# Константы для ставок комиссий
TAX_RATE = 0.06
BANK_COMMISSION_RATE = 0.02
AUTHOR_COMMISSION_RATE = 0.10
MARKETPLACE_COMMISSION_RATE = 0.20


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')

    @property
    def total_price(self):
        tax = TAX_RATE * float(self.price)
        bank_commission = BANK_COMMISSION_RATE * float(self.price)
        author_commission = AUTHOR_COMMISSION_RATE * float(self.price)
        margin = MARKETPLACE_COMMISSION_RATE * float(self.price)

        total_price = float(self.price) + tax + bank_commission + author_commission + margin
        return round(total_price, 2)

    # Метод для представления модели в виде строки
    def __str__(self):
        return f"Продукт: {self.name} "

    # Метаданные модели
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
