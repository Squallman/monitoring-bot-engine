import os

import http_helper
import keyboard_helper
import commands

TOKEN = os.getenv('TOKEN')
TELEGRAM_SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


def default(store_1_status, store_1_name,
            store_2_status, store_2_name, chat_id, text):
    store_1_message = f'{store_1_status} {store_1_name}' if store_1_name else commands.add_new
    store_2_message = f'{store_2_status} {store_2_name}' if store_2_name else commands.add_new
    keyboard = keyboard_helper.default([store_1_message, store_2_message])
    data = build_data(chat_id, keyboard, text)
    send_message(data)


def build_data(chat_id, keyboard, text):
    return {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown',
        'reply_markup': {
            'keyboard': keyboard,
            'resize_keyboard': True,
            'one_time_keyboard': True
        }
    }


def send_message(data):
    http_helper.post(TELEGRAM_SEND_URL, data)
