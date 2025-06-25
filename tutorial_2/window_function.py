
import logging
import csv
from mydb_connection import connect_to_db

logging.basicConfig(level=logging.INFO)

def windowFucntion(sql_query, database_name="tutorial2_db"):
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
            RANK() OVER (PARTITION BY c.city_name ORDER BY p.age DESC) AS age_rank_in_city
        FROM people p
        JOIN cities c ON p.city_id = c.id
        ORDER BY c.city_name, age_rank_in_city;
        """

windowFucntion(query, "tutorial2_db") 