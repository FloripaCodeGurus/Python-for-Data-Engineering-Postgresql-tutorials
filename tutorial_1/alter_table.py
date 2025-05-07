from postgres_connector import connect_to_postgres
import logging

logging.basicConfig(level=logging.INFO)

conn = connect_to_postgres(dbname="university")
if conn:
    cur = conn.cursor()
    cur.execute("ALTER TABLE people ALTER COLUMN phone_number TYPE VARCHAR(30);")
    logging.info("Column phone_number altered successfully.")
    cur.close()
    conn.close()
else:
    print("Failed to connect to PostgreSQL.")
