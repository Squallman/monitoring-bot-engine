def get_slots(db):
    sql_query = 'SELECT slot FROM auchan;'
    with db.cursor() as cursor:
        cursor.execute(sql_query)
        return cursor.fetchall()


def remove_slots(db, slots):
    for slot in slots:
        sql_query = 'DELETE FROM auchan WHERE slot = %s;'
        with db.cursor() as cursor:
            cursor.execute(sql_query, slot)
    db.commit()


def add_slots(db, slots):
    for slot in slots:
        sql_query = 'INSERT INTO auchan (slot) VALUES (%s);'
        with db.cursor() as cursor:
            cursor.execute(sql_query, slot)
    db.commit()
