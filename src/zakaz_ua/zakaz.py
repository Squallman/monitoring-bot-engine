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

lambda_handler({}, {})
# https://eztmber9qe.execute-api.us-east-1.amazonaws.com/telegram_api
# TOKEN=513357203:AAFB39a1t-mwyO2Eu318rEhgr6zLlTE1woA

# https://api.telegram.org/bot513357203:AAFB39a1t-mwyO2Eu318rEhgr6zLlTE1woA/setWebhook?url=https://eztmber9qe.execute-api.us-east-1.amazonaws.com/telegram_api