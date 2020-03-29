from unittest import TestCase, mock


class UsersTest(TestCase):

    @mock.patch('zakaz_ua.users_dao.fetch_users')
    def test_fetch_users(self, mock_fetch_users):
        mock_fetch_users.return_value = {0o001, 0o002}
        users.fetch_users('token')