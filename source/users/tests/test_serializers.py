from users.serializers import SpecializationSerializer
from users.tests.users_test_settings import UsersSettings


class SpecializationTestCase(UsersSettings):
	def test_get_serialized_specializations(self) -> None:
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

	def test_post_correct_validate_serializer(self) -> None:
		correct_data = {
			'title': 'Design',
		}
		serializer = SpecializationSerializer(data=correct_data)
		self.assertTrue(serializer.is_valid(), self.error())

	def test_post_wrong_validate_serializer(self) -> None:
		wrong_data = {
			'wrong_pole': 'wronga_data',
		}
		serializer = SpecializationSerializer(data=wrong_data)
		self.assertFalse(serializer.is_valid(), self.error())

