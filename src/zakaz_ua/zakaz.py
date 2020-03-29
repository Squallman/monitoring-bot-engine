from src.zakaz_ua import http_helper
import users
import auchan
import os
import json

token = os.getenv('TOKEN')


def lambda_handler(event, context):

    user_set = users.fetch_users(token)
    messages = auchan.get_auchan_changes()

    for user_id in user_set:
        for message in messages:
            http_helper.telegram_send_message(token, user_id, message)
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
