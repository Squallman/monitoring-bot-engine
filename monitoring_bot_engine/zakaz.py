import json

import store_dao
import store_api
import store_status
import user_dao
import telegram_api


def lambda_handler(event, context):

    store_list = store_dao.get_stores()
    items = [item for store in store_list for item in store_api.get_store_slots(
        store.get('store_id'), store.get('store_name'), store.get('location')
    )]
    processed_items = store_status.process_slots(items)
    users = user_dao.get_users()
    for user in users:
        user_store_list = [element for element in processed_items
                           if user.get('store_1') == element.get('store_id')
                           and user.get('store_1_status')]
        user_store_list.extend([element for element in processed_items
                                if user.get('store_2') == element.get('store_id')
                                and user.get('store_2_status')])
        sorted_list = sorted(user_store_list, key=lambda element: element.get('title'))
        message_list = store_api.build_store_result_message(sorted_list)
        default_message(user.get('chat_id'), message_list)

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }


def default_message(chat_id, text):
    user = user_dao.get_user(chat_id)
    chat_id = user.get('chat_id')
    store_1_status = '✅' if user.get('store_1_status') == 1 \
        else '❌' if user.get('store_1_status') is not None else ''
    store_2_status = '✅' if user.get('store_2_status') == 1 \
        else '❌' if user.get('store_2_status') is not None else ''
    store_1_name = user.get('store_1_name')
    store_2_name = user.get('store_2_name')
    return telegram_api.default(store_1_status, store_1_name,
                                store_2_status, store_2_name, chat_id, text)
