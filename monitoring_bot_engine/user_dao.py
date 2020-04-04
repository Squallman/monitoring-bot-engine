def fetch_users(db):
    sql_query = 'SELECT user_id FROM tbl_user;'
    with db.cursor() as cursor:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        print('fetched result:')
        print(result)
        return result
