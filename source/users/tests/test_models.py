from django.test import TestCase
from django.db.utils import IntegrityError, DataError

from .users_test_settings import UsersSettings
from ..models import Profile, Skill


class SkillModelTestCase(UsersSettings):
    def test_create_instance_positive(self) -> None:
        self.assertEqual(self.test_skill1.title, 'Django_test_skill', self.error())

    def test_cant_create_instance_copy_negative(self) -> None:
        with self.assertRaises(IntegrityError):
            Skill.objects.create(title='Django_test_skill')

    def test_invalid_filed_data_negative(self) -> None:
        with self.assertRaises(DataError):
            Skill.objects.create(title='a' * 51)

    def test_skill_meta_poles(self) -> None:
        self.assertEqual(self.test_skill1._meta.verbose_name, 'Технология', self.error())
        self.assertEqual(self.test_skill1._meta.verbose_name_plural, 'Технологии', self.error())

    def test_skill_str_view(self) -> None:
        value = 'Django_test_skill'
        self.assertEqual(str(self.test_skill1), value, self.error())


# class ProfileModelTestCase(Settings):
#
#     def test_create_instance_positive(self) -> None:
#         test_skill = Skill.objects.create(title='Django_test_skill')
#         self.assertEqual(test_skill.title, 'Django_test_skill')