from unittest import TestCase, mock

from zakaz_ua import users

class UsersTest(TestCase):

    @mock.patch('zakaz_ua.user_dao.add_user')
    @mock.patch('zakaz_ua.user_dao.fetch_users')
    @mock.patch('zakaz_ua.http_helper.telegram_get_updates')
    def test_fetch_users(self, mock_telegram_get_updates, mock_fetch_users, mock_add_user):
        mock_telegram_get_updates.return_value = \
            {'result': [{ 'message': {'from': {'id': 3}, 'text': 'start'}}]}
        mock_fetch_users.return_value = {1, 2}
        user_set = users.fetch_users('token')
        self.assertSetEqual(user_set, {1, 2, 3})
        self.assertEqual(mock_add_user.call_count, 1)

    @mock.patch('zakaz_ua.user_dao.add_user')
    @mock.patch('zakaz_ua.user_dao.fetch_users')
    @mock.patch('zakaz_ua.http_helper.telegram_get_updates')
    def test_fetch_users_without_adding(self, mock_telegram_get_updates, mock_fetch_users,
                                        mock_add_user):
        mock_telegram_get_updates.return_value = \
            {'result': [{ 'message': {'from': {'id': 3}, 'text': 'test'}}]}
        mock_fetch_users.return_value = {1, 2}
        user_set = users.fetch_users('token')
        self.assertSetEqual(user_set, {1, 2})
        self.assertEqual(mock_add_user.call_count, 0)

    @mock.patch('zakaz_ua.user_dao.remove_user')
    @mock.patch('zakaz_ua.user_dao.fetch_users')
    @mock.patch('zakaz_ua.http_helper.telegram_get_updates')
    def test_fetch_users_with_remove(self, mock_telegram_get_updates, mock_fetch_users,
                                     mock_remove_user):
        mock_telegram_get_updates.return_value = \
            {'result': [{'message': {'from': {'id': 2}, 'text': 'stop'}}]}
        mock_fetch_users.return_value = {1, 2}
        user_set = users.fetch_users('token')
        self.assertSetEqual(user_set, {1})
        self.assertEqual(mock_remove_user.call_count, 1)
