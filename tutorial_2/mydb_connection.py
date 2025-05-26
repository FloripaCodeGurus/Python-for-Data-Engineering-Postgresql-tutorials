import psycopg2

def connect_to_db(database_name):
    try:
        conn = psycopg2.connect(
        dbname=database_name,
        user="postgres",
        password="88454699",
        host="localhost",
        port="5432"
    )
        conn.autocommit = True
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None 