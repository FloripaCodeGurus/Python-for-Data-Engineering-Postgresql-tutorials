
import logging
from mydb_connection import connect_to_db

logging.basicConfig(level=logging.INFO)

def caseWhen(sql_query, database_name="tutorial2_db"):
    try:
        conn = connect_to_db(database_name)
        if conn:
            cur = conn.cursor()
            cur.execute(sql_query)
            rows = cur.fetchall()
            for row in rows:
                print(row)
            cur.close()
            conn.close()
        else:
            logging.info("Failed to connect to PostgreSQL.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")

query = """
        SELECT
            p.first_name || ' ' || p.last_name AS full_name,
            p.age,
            c.city_name,
            CASE
                WHEN p.age < 30 THEN 'Young'
                WHEN p.age BETWEEN 30 AND 60 THEN 'Adult'
                ELSE 'Senior'
            END AS age_group
        FROM people p
        JOIN cities c ON p.city_id = c.id
        ORDER BY age_group, p.age;
                """

caseWhen(query, "tutorial2_db") 