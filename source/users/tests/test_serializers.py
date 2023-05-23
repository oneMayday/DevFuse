from users.serializers import SpecializationSerializer, TechnologieSerializer, ReadProfileSerializer, \
	CreateAndUpdateProfileSerializer
from users.tests.users_test_settings import UsersSettings


class SpecializationSerializerTestCase(UsersSettings):
	def test_get_specializations_serialized(self) -> None:
		serializer = SpecializationSerializer([self.test_specialization1, self.test_specialization2], many=True)
		expected_data = [
			{
				'id': self.test_specialization1.pk,
				'title': 'Backend',
			},
			{
				'id': self.test_specialization2.pk,
				'title': 'Frontend',
			}
		]
		self.assertEqual(serializer.data, expected_data, self.error())

	def test_post_correct_validate_specialization_serializer(self) -> None:
		correct_data = {
			'title': 'Design',
		}
		serializer = SpecializationSerializer(data=correct_data)
		self.assertTrue(serializer.is_valid(), self.error())

	def test_post_wrong_validate_specialization_serializer(self) -> None:
		wrong_data = {
			'wrong_pole': 'wronga_data',
		}
		serializer = SpecializationSerializer(data=wrong_data)
		self.assertFalse(serializer.is_valid(), self.error())


class TechnologiesSerializerTestCase(UsersSettings):
	def test_get_serialized_technologies(self) -> None:
		serializer = TechnologieSerializer([self.test_technologie1, self.test_technologie2], many=True)
		expected_data = [
			{
				'id': self.test_technologie1.pk,
				'title': 'Django_test_skill',
			},
			{
				'id': self.test_technologie2.pk,
				'title': 'JavaScript_test_skill',
			}
		]
		self.assertEqual(serializer.data, expected_data, self.error())

	def test_post_correct_validate_technologie_serializer(self) -> None:
		correct_data = {
			'title': 'React_test_skill',
		}
		serializer = SpecializationSerializer(data=correct_data)
		self.assertTrue(serializer.is_valid(), self.error())

	def test_post_wrong_validate_technologie_serializer(self) -> None:
		wrong_data = {
			'wrong_pole': 'wronga_data',
		}
		serializer = SpecializationSerializer(data=wrong_data)
		self.assertFalse(serializer.is_valid(), self.error())


class ProfileSerializerTestCase(UsersSettings):
	def test_get_detail_serialized_profiles(self) -> None:
		serializer = ReadProfileSerializer(self.test_profile1)
		expected_data = {
				'name': 'test_user1_name',
				'surname': 'test_user1_surname',
				'city': 'default_City1',
				'about': 'Something about test_user1',
				'specialization': self.test_specialization1.title,
				'skills': [self.test_technologie1.title, self.test_technologie2.title],
				'telegram': 'https://t.me/TestUser1',
				'github': 'https://github.com',
			}
		self.assertEqual(serializer.data, expected_data, self.error())

	def test_get_list_serialized_profiles(self) -> None:
		serializer = ReadProfileSerializer([self.test_profile1, self.test_profile2], many=True)
		expected_data = [
			{
				'name': 'test_user1_name',
				'surname': 'test_user1_surname',
				'city': 'default_City1',
				'about': 'Something about test_user1',
				'specialization': self.test_specialization1.title,
				'skills': [self.test_technologie1.title, self.test_technologie2.title],
				'telegram': 'https://t.me/TestUser1',
				'github': 'https://github.com',
			},
			{
				'name': 'test_user2_name',
				'surname': 'test_user2_surname',
				'city': 'default_City1',
				'about': 'Something about test_user2',
				'specialization': self.test_specialization2.title,
				'skills': [self.test_technologie3.title, self.test_technologie4.title],
				'telegram': 'https://t.me/TestUser2',
				'github': 'https://github.com',
			},
		]
		self.assertEqual(serializer.data, expected_data, self.error())

	def test_post_correct_validate_profile_serializer(self) -> None:
		correct_data = {
				'name': 'test_name',
				'surname': 'test_surname',
				'city': 'default_City',
				'about': 'Something about test_user',
				'specialization': self.test_specialization1.pk,
				'skills': [self.test_technologie2.pk, self.test_technologie4.pk],
				'telegram': 'https://t.me/TestUser',
				'github': 'https://github.com',
			}
		serializer = CreateAndUpdateProfileSerializer(data=correct_data)
		self.assertTrue(serializer.is_valid, self.error())

	def test_update_correct_validate_profile_serializer(self) -> None:
		correct_update_data = {
				'name': 'test_name_updated',
				'surname': 'test_surname_updated',
			}
		serializer = CreateAndUpdateProfileSerializer(data=correct_update_data)
		self.assertTrue(serializer.is_valid, self.error())
