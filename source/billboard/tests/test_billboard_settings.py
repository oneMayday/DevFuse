from unittest import TestCase

from django.contrib.auth.models import User
from django.test.client import Client

from billboard.models import Publication
from users.models import Technologie, Specialization


class BillboardSettings(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # Create test specializations
        cls.test_specialization1 = Specialization.objects.create(title='Backend')
        cls.test_specialization2 = Specialization.objects.create(title='Frontend')
        cls.test_specialization3 = Specialization.objects.create(title='DevOps')
        cls.test_specialization4 = Specialization.objects.create(title='Fullstack')

        # Create test skills
        cls.test_technologie1 = Technologie.objects.create(title='Django_test_skill')
        cls.test_technologie2 = Technologie.objects.create(title='JavaScript_test_skill')
        cls.test_technologie3 = Technologie.objects.create(title='Python_test_skill')
        cls.test_technologie4 = Technologie.objects.create(title='React_test_skill')

        # Create users
        cls.test_user1 = User.objects.create_user(
            username='test_user1',
            password='testuser1_password',
            is_superuser=True,
            is_staff=True,
        )
        cls.authorized_user1 = Client()
        cls.authorized_user1.login(username='test_user1', password='testuser1_password')

        cls.test_user2 = User.objects.create_user(
            username='test_user2',
            password='testuser2_password',
        )
        cls.authorized_user2 = Client()
        cls.authorized_user2.login(username='test_user2', password='testuser2_password')

        cls.test_user3 = User.objects.create_user(
            username='test_user3',
            password='testuser3_password',
        )
        cls.authorized_user3 = Client()
        cls.authorized_user3.login(username='test_user3', password='testuser3_password')

        cls.test_user4 = User.objects.create_user(
            username='test_user4',
            password='testuser4_password',
        )
        cls.authorized_user4 = Client()
        cls.authorized_user4.login(username='test_user4', password='testuser4_password')

        # Anonymous user.
        cls.guest_user = Client()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def error(self) -> str:
        error_lenght = len(str(self.id()))
        error_msg = f'\n{24 * "-" + error_lenght * "-"}\n' \
                    f'--- Ошибка в тесте: {self.id()} ---\n' \
                    f'{24 * "-" + error_lenght * "-"}'
        return error_msg
