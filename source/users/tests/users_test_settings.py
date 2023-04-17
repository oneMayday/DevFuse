from django.test import TestCase

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

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def error(self) -> str:
        error_lenght = len(str(self.id()))
        error_msg = f'\n{24 * "-" + error_lenght * "-"}\n' \
                    f'--- Ошибка в тесте: {self.id()} ---\n' \
                    f'{24 * "-" + error_lenght * "-"}'
        return error_msg
