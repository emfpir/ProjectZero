import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            database='',
            user='',
            password='',
            host='',
            port=''
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn

connection = create_connection()