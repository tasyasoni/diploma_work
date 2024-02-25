from django.db import models
from django.contrib.auth.models import AbstractUser


# Определение модели пользователей, наследующей абстрактную модель пользователя
class Users(AbstractUser):
    # Убираем поле "username", так как мы будем использовать "email" вместо него
    username = None
    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты пользователя")
    seller_status = models.BooleanField(default=False, verbose_name="Статус продавца")

    # Указываем, что поле "email" будет использоваться для идентификации пользователя
    USERNAME_FIELD = "email"
    # Поля, которые будут запрашиваться при создании пользователя через команду createsuperuser
    REQUIRED_FIELDS = []

    # Метод для представления модели в виде строки
    def __str__(self):
        return f"{self.email}"

    # Метаданные модели
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'
