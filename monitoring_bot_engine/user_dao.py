import os
import pymysql
from pymysql.cursors import DictCursor

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

DB = pymysql.connect(
    host=DB_HOST,
    port=int(DB_PORT),
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

COLUMNS = ['chat_id', 'location', 'store_1', 'store_2', 'store_1_status', 'store_2_status',
           'first_name', 'last_name', 'location_confirm', 'store_1_name', 'store_2_name']


def get_users():
    columns = ','.join(COLUMNS)
    select_query = f'SELECT {columns} FROM state WHERE store_1_status = 1 or store_2_status = 1'
    with DB.cursor(DictCursor) as cursor:
        cursor.execute(select_query)
        return cursor.fetchall()


def get_user(chat_id):
    fields = ','.join(COLUMNS)
    sql_query = f'SELECT {fields} FROM state WHERE chat_id = %s;'
    with DB.cursor(DictCursor) as cursor:
        cursor.execute(sql_query, chat_id)
        return cursor.fetchone()
