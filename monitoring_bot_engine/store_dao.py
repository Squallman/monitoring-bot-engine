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
    port=3306,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

COLUMNS = ['chat_id', 'store_id', 'store_hash', 'location', 'store_name']


def get_stores():
    query = """
        SELECT DISTINCT
            store_id, location, store_name
        FROM
            store;
    """
    with DB.cursor(DictCursor) as cursor:
        cursor.execute(query)
        return cursor.fetchall()
