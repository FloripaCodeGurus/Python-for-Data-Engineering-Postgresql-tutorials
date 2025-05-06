import psycopg2

def connect_to_university_db():
    try:
        conn = psycopg2.connect(
        dbname="university",
        user="postgres",
        password="frc47521122",
        host="localhost",
        port="5433"
    )
        conn.autocommit = True
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None 
