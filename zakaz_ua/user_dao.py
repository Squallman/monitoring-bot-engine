users = set()


def fetch_users():
    return users


def add_user(user_id):
    users.add(user_id)


def remove_user(user_id):
    users.remove(user_id)
