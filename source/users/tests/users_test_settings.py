from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from users.models import Skill, Profile


class UsersSettings(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # Create test skills
        cls.test_skill1 = Skill.objects.create(title='Django_test_skill')
        cls.test_skill2 = Skill.objects.create(title='JavaScript_test_skill')
        cls.test_skill3 = Skill.objects.create(title='Python_test_skill')
        cls.test_skill4 = Skill.objects.create(title='React_test_skill')

        # Create users
        cls.test_user1 = User.objects.create_user(
            username='test_user1',
            password='testuser1_password',
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
            nickname='test_user1_nickname',
            name='test_user1_name',
            surname='test_user1_surname',
            email='test_user1@test.com',
            city='default_City1',
            about='Something about test_user1',
            telegram='https://t.me/TestUser1',
            github='https://github.com',
        )
        cls.test_profile1.skills.set([cls.test_skill1, cls.test_skill2])

        cls.test_profile2 = Profile.objects.create(
            user=cls.test_user2,
            nickname='test_user2_nickname',
            name='test_user2_name',
            surname='test_user2_surname',
            email='test_user2@test.com',
            city='default_City1',
            about='Something about test_user2',
            telegram='https://t.me/TestUser2',
            github='https://github.com',
        )
        cls.test_profile2.skills.set([cls.test_skill3, cls.test_skill4])

        cls.test_profile3 = Profile.objects.create(
            user=cls.test_user3,
            nickname='test_user3_nickname',
            name='test_user3_name',
            surname='test_user3_surname',
            email='test_user3@test.com',
            city='default_City2',
            about='Something about test_user3',
            telegram='https://t.me/TestUser3',
            github='https://github.com',
        )
        cls.test_profile3.skills.set([cls.test_skill1, cls.test_skill3])

        cls.test_profile4 = Profile.objects.create(
            user=cls.test_user4,
            nickname='test_user4_nickname',
            name='test_user4_name',
            surname='test_user4_surname',
            email='test_user4@test.com',
            city='default_City2',
            about='Something about test_user4',
            telegram='https://t.me/TestUser4',
            github='https://github.com',
        )
        cls.test_profile4.skills.set([cls.test_skill2, cls.test_skill4])

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def error(self) -> str:
        error_lenght = len(str(self.id()))
        error_msg = f'\n{24 * "-" + error_lenght * "-"}\n' \
                    f'--- Ошибка в тесте: {self.id()} ---\n' \
                    f'{24 * "-" + error_lenght * "-"}'
        return error_msg
