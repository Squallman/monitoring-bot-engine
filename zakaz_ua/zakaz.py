import http_helper
import users
import auchan
import os
import pymysql
import json

from pymysql.cursors import DictCursor

token = os.getenv('TOKEN')

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

DB = pymysql.connect(
    host=DB_HOST,
    port=3306,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    cursorclass=DictCursor
)


def lambda_handler(event, context):

    user_set = users.fetch_users(DB)
    messages = auchan.get_auchan_changes(DB)

    for user_id in user_set:
        for message in messages:
            http_helper.telegram_send_message(token, user_id, message)
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
