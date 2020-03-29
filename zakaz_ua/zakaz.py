from zakaz_ua import users, auchan, http_helper
import os

token = os.getenv('TOKEN')

if not token:
    exit(1)

users = users.fetch_users(token)
messages = auchan.get_auchan_changes()

for user_id in users:
    for message in messages:
        http_helper.telegram_send_message(token, user_id, message)

