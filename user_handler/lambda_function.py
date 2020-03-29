import json
import os
import requests

TELEGRAM_SEND_URL = 'https://api.telegram.org/bot%(token)s/sendMessage?chat_id=%(chat_id)s' \
                    '&parse_mode=Markdown&text=%(message)s'

TOKEN = os.getenv('TOKEN')


def lambda_handler(event, context):

    if 'message' in event:
        message = event.get('message')
        text = message.get('text') if 'text' in message else ''
        chat = message.get('chat') if 'chat' in message else ''
        chat_id = chat.get('id') if 'id' in chat else ''
        if 'start' in text.lower():
            t_message = '👍Looking for available slots was started'
            telegram_send_message(TOKEN, chat_id, t_message)
        elif 'stop' in text.lower():
            t_message = '👎Looking for available slots was stoped'
            telegram_send_message(TOKEN, chat_id, t_message)
        else:
            t_message = '🤦Bot doesn\'t support this command, try "start" or "stop"'
            telegram_send_message(TOKEN, chat_id, t_message)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def telegram_send_message(token, chat_id, message):
    params = {'token': token, 'chat_id': chat_id, 'message': message}
    requests.get(url=TELEGRAM_SEND_URL % params)