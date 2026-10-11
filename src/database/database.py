import os

import psycopg2
from psycopg2.extras import execute_values


def get_connection():
    return psycopg2.connect(
        host=os.environ["POSTGRES_HOST"],
        port=os.environ["POSTGRES_PORT"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        dbname=os.environ["POSTGRES_DB"],
    )


def clear_expenses():
    connection = get_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE exp RESTART IDENTITY")
    finally:
        connection.close()


def insert_data_to_db(rows):
    values = [(row.name, row.amount, row.category) for row in rows]
    connection = get_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                execute_values(
                    cursor,
                    "INSERT INTO exp (name, amount, category) VALUES %s",
                    values,
                    page_size=100,
                )
    finally:
        connection.close()