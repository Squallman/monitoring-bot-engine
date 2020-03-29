from zakaz_ua import auchan_dao, http_helper

data_key = 'data'
items_key = 'items'
windows_key = 'windows'
date_key = 'date'
title_key = 'title'
is_available_key = 'is_available'

PAYLOAD = {'meta': {}, 'request': [{
        'args': {
            'store_id': '48246409', 'zone_id': 'lviv_shevchenkivskii-b', 'delivery_type': 'plan'
        }, 'v': '0.1', 'type': 'user.set_zone', 'id': {
            'store_id': '48246409', 'zone_id': 'lviv_shevchenkivskii-b', 'delivery_type': 'plan'
        }
    }, {
        'args': {
            'store_ids': ['48246409']
        }, 'v': '0.1', 'type': 'store.list', 'id': 'store'
    }, {
        'args': {
            'store_id': '48246409'
        }, 'v': '0.1', 'type': 'user.info', 'id': 'user_info'
    }, {
        'args': {
            'store_ids': ['48246409'], 'only_available': False,
            'zone_id': 'lviv_shevchenkivskii-b', 'delivery_type': 'plan'
        }, 'v': '0.1', 'type': 'timewindows.list', 'id': 'timewindows_list'
    }, {
        'args': {
            'store_id': '48246409', 'revision': 2, 'contract_id': None, 'payment_method': None
        }, 'v': '0.1', 'type': 'cart.state', 'id': 'cart'
    }]}


def perform_auchan_request():
    responses = http_helper.get_auchan_dates(PAYLOAD)
    auchan_windows = []
    for resp in responses:
        data = resp.get(data_key)
        if items_key in data:
            items = data.get(items_key)
            for item in items:
                if windows_key in item:
                    windows = item.get(windows_key)
                    for window in windows:
                        date = window.get(date_key)
                        window_list = window.get(windows_key)
                        auchan_windows.extend([{
                            title_key: f'{date} {window_item.get(title_key)}',
                            is_available_key: bool(window_item.get(is_available_key))
                        } for window_item in window_list])
    return [res.get(title_key) for res in auchan_windows if res.get(is_available_key)]


def get_auchan_changes():
    available_list = perform_auchan_request()
    previous_list = auchan_dao.get_slots()
    new_slots = compare_list(available_list, previous_list)
    removed_slots = compare_list(previous_list, available_list)
    auchan_dao.remove_slots(removed_slots)
    auchan_dao.add_slots(new_slots)
    messages = prepare_messages(new_slots, removed_slots)
    return sorted(messages)


def compare_list(list_1, list_2):
    return [elem for elem in list_1 if elem not in list_2]


def prepare_messages(new_slots, removed_slots):
    new_messages = [f'✅ {slot} available' for slot in new_slots]
    removed_messages = [f'❌ {slot} closed' for slot in removed_slots]
    return new_messages + removed_messages
