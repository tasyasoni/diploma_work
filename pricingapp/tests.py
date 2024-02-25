from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from usersapp.models import Users


class PriceCreateView(TestCase):
    def setUp(self):
        """
        Подготовка к тестированию. Создаем пользователя, аутентифицируем его и создаем клиента API.
        """
        self.user = Users(
            email="test@yandex.ru",
            password="test",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            seller_status=True,
        )

        self.user.set_password("test")
        self.user.save()

        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_calculate_price(self):
        """
        Тестирование расчета цены при создании товара.

        Создаем товар с заданной ценой и проверяем, что расчет цены происходит правильно.
        """
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": "10.00"
        }

        response = self.client.post('/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("total_price", response.data)

        # Проверяем, что цена правильно рассчитана с помощью assertAlmostEqual
        total_price = float(response.data['total_price'])
        expected_price = 10.0 + (0.06 * 10.0) + (0.02 * 10.0) + (0.10 * 10.0) + (0.20 * 10.0)
        self.assertAlmostEqual(total_price, expected_price, delta=0.01)

    def test_unauthenticated_create_product(self):
        """
        Тест на создание товара без аутентификации.

        Попытка создания товара без предоставления аутентификации должна вернуть 401 Unauthorized.
        """
        client = APIClient()
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": "10.00"
        }
        response = client.post('/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_negative_price(self):
        """
        Тест на отрицательную цену.

        Попытка создания товара с отрицательной ценой должна вернуть 400 Bad Request.
        """
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": "-10.00"
        }
        response = self.client.post('/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculate_price_with_zero_price(self):
        """
        Тест на расчет цены с нулевой ценой.

        Создаем товар с нулевой ценой и проверяем, что такой товар создаваться не должен.
        """
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": "0.00"
        }
        response = self.client.post('/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
