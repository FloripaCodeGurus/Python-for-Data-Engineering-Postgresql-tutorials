from postgres_connector import connect_to_postgres
import logging


def create_database(database_name):
    conn = connect_to_postgres()
    if conn:
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS{database_name};")
        cur.close()
        conn.close()
        logging.info(f"Database {database_name} created successfully.")
    else:
        logging.info("Failed to connect to PostgreSQL.")


create_database="tutorial2_db"