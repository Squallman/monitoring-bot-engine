import user_dao


def fetch_users(db):
    users = user_dao.fetch_users(db)
    return set(users)