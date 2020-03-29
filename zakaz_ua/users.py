from zakaz_ua import http_helper, user_dao


def fetch_users(token):
    users = user_dao.fetch_users()
    new_users = fetch_new_users(token)
    for user_id, message in new_users.items():
        if 'start' in message.lower() and user_id not in users:
            users.add(user_id)
            user_dao.add_user(user_id)
        elif message.lower() == 'stop' and user_id in users:
            users.remove(user_id)
            user_dao.remove_user(user_id)
    return users


def fetch_new_users(token):
    fetch_result = http_helper.telegram_get_updates(token)
    result_list = fetch_result.get('result')
    return {result.get('message').get('from').get('id'): result.get('message').get('text')
            for result in result_list}
