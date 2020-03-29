import requests, json

TELEGRAM_SEND_URL = 'https://api.telegram.org/bot%(token)s/sendMessage?chat_id=%(chat_id)s' \
                    '&parse_mode=Markdown&text=%(message)s'
TELEGRAM_GET_UPDATES_URL = 'https://api.telegram.org/bot%(token)s/getUpdates'
AUCHAN_GET_URL = 'https://auchan.zakaz.ua/api/query.json'


def get_auchan_dates(payload):
    data = json.dumps(payload)
    content = requests.post(url=AUCHAN_GET_URL, data=data).json()
    return content.get('responses')


def telegram_send_message(token, chat_id, message):
    params = {'token': token, 'chat_id': chat_id, 'message': message}
    requests.get(url=TELEGRAM_SEND_URL%params)


def telegram_get_updates(token):
    params = {'token': token}
    response = requests.get(TELEGRAM_GET_UPDATES_URL%params)
    return response.json()