from rest_framework import serializers
from usersapp.models import Users


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Users.

    Этот сериализатор используется для преобразования объектов Users в формат JSON и обратно.
    Он определяет, какие поля модели должны быть сериализованы.

    """

    class Meta:
        model = Users
        fields = ["id", "email", 'password', 'seller_status', 'first_name']


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации новых пользователей.

    Этот сериализатор используется для создания новых пользователей на основе данных,
    предоставленных клиентом. Он также выполняет проверку и валидацию данных перед созданием
    нового пользователя.

    Поля:
    - email: Email-адрес пользователя.
    - password: Пароль пользователя.
    - password2: Подтверждение пароля.
    - seller_status: Флаг, указывающий, является ли пользователь продавцом.

    Методы:
    - save(): Создает нового пользователя на основе предоставленных данных.
    - Проверяет, что пароль и подтверждение пароля совпадают.
    - Устанавливает пароль пользователя и сохраняет его.

    """

    password2 = serializers.CharField()
    seller_status = serializers.BooleanField(required=False)  # Определяем seller_status как необязательное поле

    class Meta:
        model = Users
        fields = ['email', 'password', 'password2', 'seller_status']

    def save(self, *args, **kwargs):
        """
        Создает и сохраняет нового пользователя.
        Проверяет, что пароль и подтверждение пароля совпадают, затем создает нового пользователя
        на основе предоставленных данных. Устанавливает пароль пользователя и сохраняет его в базе данных.
        Возвращает созданного пользователя.

        """
        user = Users(
            email=self.validated_data['email'],
            first_name=self.validated_data['email'],
            last_name=self.validated_data['email'],
            is_superuser=False,
            is_staff=False,
            is_active=True,
            seller_status=self.validated_data.get('seller_status', False)  # Используем get для чтения значения seller_status
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"password": "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user
