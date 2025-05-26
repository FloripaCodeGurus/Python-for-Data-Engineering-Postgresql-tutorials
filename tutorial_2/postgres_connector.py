import psycopg2

def connect_to_postgres(dbname="postgres"):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
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

# conn = connect_to_postgres()
# if conn:
#     cur = conn.cursor()
#     cur.execute("SELECT version();")
#     db_version = cur.fetchone()
#     print(f"PostgreSQL version: {db_version[0]}")
#     cur.close()
#     conn.close()



