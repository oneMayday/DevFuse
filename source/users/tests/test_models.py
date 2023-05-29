from django.db.utils import IntegrityError, DataError

from .global_test_settings import UsersSettings
from ..models import Profile, Technologie, Specialization


class SpecializationsModelTestCase(UsersSettings):
    def test_specialization_fileds(self) -> None:
        self.assertEqual(self.test_specialization1.title, 'Backend', self.error())

    def test_cant_create_specialization_with_the_same_name(self) -> None:
        with self.assertRaises(IntegrityError):
            Specialization.objects.create(title='Backend')


class TechnologieModelTestCase(UsersSettings):
    def test_technologie_fileds(self) -> None:
        self.assertEqual(self.test_technologie1.title, 'Django_test_skill', self.error())

    def test_cant_create_technology_with_the_same_name(self) -> None:
        with self.assertRaises(IntegrityError):
            Technologie.objects.create(title='Django_test_skill')

    def test_invalid_field_data_(self) -> None:
        with self.assertRaises(DataError):
            Technologie.objects.create(title='a' * 51)

    def test_technologie_meta_poles(self) -> None:
        self.assertEqual(self.test_technologie1._meta.verbose_name, 'Технология', self.error())
        self.assertEqual(self.test_technologie1._meta.verbose_name_plural, 'Технологии', self.error())

    def test_technologie_str_view(self) -> None:
        self.assertEqual(str(self.test_technologie1), 'Django_test_skill', self.error())


class ProfileModelTestCase(UsersSettings):
    def test_profile_fields(self) -> None:
        self.assertEqual(self.test_profile1.user, self.test_user1, self.error())
        self.assertEqual(self.test_profile1.name, 'test_user1_name', self.error())
        self.assertEqual(self.test_profile1.surname, 'test_user1_surname', self.error())
        self.assertEqual(self.test_profile1.city, 'default_City1', self.error())
        self.assertEqual(self.test_profile1.specialization, self.test_specialization1, self.error())
        self.assertFalse(self.test_profile1.ready_to_work, self.error())
        self.assertEqual(self.test_profile1.about, 'Something about test_user1', self.error())
        self.assertEqual(self.test_profile1.telegram, 'https://t.me/TestUser1', self.error())
        self.assertEqual(self.test_profile1.github, 'https://github.com', self.error())
        self.assertEqual(
            [skill for skill in self.test_profile1.skills.all()],
            [self.test_technologie1, self.test_technologie2],
            self.error()
        )

    def test_profile_meta_poles(self) -> None:
        self.assertEqual(self.test_profile1._meta.verbose_name, 'Профиль', self.error())
        self.assertEqual(self.test_profile1._meta.verbose_name_plural, 'Профили', self.error())

    def test_profile_user_cant_get_two_profiles(self) -> None:
        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=self.test_user1)

    def test_profile_wrong_name(self) -> None:
        with self.assertRaises(DataError):
            Profile.objects.create(name='a' * 51)

    def test_profile_wrong_surname(self) -> None:
        with self.assertRaises(DataError):
            Profile.objects.create(surname='a' * 51)

    def test_profile_wrong_city(self) -> None:
        with self.assertRaises(DataError):
            Profile.objects.create(city='a' * 51)
