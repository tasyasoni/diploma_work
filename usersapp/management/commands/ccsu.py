from django.core.management import BaseCommand
from usersapp.models import Users


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = Users.objects.create(
            email='admin@yandex.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('1234')
        user.save()
