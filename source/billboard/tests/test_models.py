from users.tests.global_test_settings import UsersSettings


class PublicationModelTestCase(UsersSettings):
    def test_profile_fields(self) -> None:
        self.assertEqual(self.test_publication1.title, 'Test_publication1', self.error())
        self.assertEqual(self.test_publication1.description, 'Test_publication1_description', self.error())
        self.assertEqual(
            [technologie for technologie in self.test_publication1.technology_stack.all()],
            [self.test_technologie1, self.test_technologie2, self.test_technologie3, self.test_technologie4],
            self.error()
        )
        self.assertEqual(
            [person for person in self.test_publication1.who_needs.all()],
            [self.test_specialization1, self.test_specialization2, self.test_specialization3],
            self.error()

        )
        self.assertEqual(self.test_publication1.owner, self.test_user1, self.error())
        self.assertEqual(
            [user for user in self.test_publication1.team.all()],
            [self.test_user1, self.test_user2],
            self.error()
        )

    def test_profile_meta_poles(self) -> None:
        self.assertEqual(self.test_publication1._meta.verbose_name, 'Публикация', self.error())
        self.assertEqual(self.test_publication1._meta.verbose_name_plural, 'Публикации', self.error())
