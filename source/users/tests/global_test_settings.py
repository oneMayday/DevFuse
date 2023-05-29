from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from billboard.models import Publication
from users.models import Technologie, Profile, Specialization


class UsersSettings(TestCase):
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

        # Create test profiles
        cls.test_profile1 = Profile.objects.create(
            user=cls.test_user1,
            name='test_user1_name',
            surname='test_user1_surname',
            city='default_City1',
            about='Something about test_user1',
            specialization=cls.test_specialization1,
            telegram='https://t.me/TestUser1',
            github='https://github.com',
        )
        cls.test_profile1.skills.set([cls.test_technologie1, cls.test_technologie2])

        cls.test_profile2 = Profile.objects.create(
            user=cls.test_user2,
            name='test_user2_name',
            surname='test_user2_surname',
            city='default_City1',
            about='Something about test_user2',
            specialization=cls.test_specialization2,
            ready_to_work=True,
            telegram='https://t.me/TestUser2',
            github='https://github.com',
        )
        cls.test_profile2.skills.set([cls.test_technologie3, cls.test_technologie4])

        cls.test_profile3 = Profile.objects.create(
            user=cls.test_user3,
            name='test_user3_name',
            surname='test_user3_surname',
            city='default_City2',
            about='Something about test_user3',
            specialization=cls.test_specialization2,
            telegram='https://t.me/TestUser3',
            github='https://github.com',
        )
        cls.test_profile3.skills.set([cls.test_technologie1, cls.test_technologie3])

        cls.test_profile4 = Profile.objects.create(
            user=cls.test_user4,
            name='test_user4_name',
            surname='test_user4_surname',
            city='default_City2',
            about='Something about test_user4',
            specialization=cls.test_specialization3,
            ready_to_work=True,
            telegram='https://t.me/TestUser4',
            github='https://github.com',
        )
        cls.test_profile4.skills.set([cls.test_technologie2, cls.test_technologie4])

        # Create publications
        cls.test_publication1 = Publication.objects.create(
            title='Test_publication1',
            description='Test_publication1_description',
            owner=cls.test_user1,
        )
        cls.test_publication1.technology_stack.set(
            [
                cls.test_technologie1,
                cls.test_technologie2,
                cls.test_technologie3,
                cls.test_technologie4
            ]
        )

        cls.test_publication1.who_needs.set(
            [
                cls.test_specialization1,
                cls.test_specialization2,
                cls.test_specialization3
            ]
        )

        cls.test_publication1.team.set([cls.test_user1, cls.test_user2])

        cls.test_publication2 = Publication.objects.create(
            title='Test_publication1',
            description='Test_publication1_description',
            owner=cls.test_user3,
        )

        cls.test_publication2.technology_stack.set(
            [
                cls.test_technologie1,
                cls.test_technologie2,
                cls.test_technologie3,
                cls.test_technologie4
            ]
        )

        cls.test_publication2.who_needs.set(
            [
                cls.test_specialization1,
                cls.test_specialization2,
                cls.test_specialization3
            ]
        )

        cls.test_publication2.team.set([cls.test_user1, cls.test_user2, cls.test_user3, cls.test_user4])

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def error(self) -> str:
        error_lenght = len(str(self.id()))
        error_msg = f'\n{24 * "-" + error_lenght * "-"}\n' \
                    f'--- Ошибка в тесте: {self.id()} ---\n' \
                    f'{24 * "-" + error_lenght * "-"}'
        return error_msg
