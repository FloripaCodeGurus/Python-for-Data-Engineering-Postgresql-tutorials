
import logging
import csv
from mydb_connection import connect_to_db

logging.basicConfig(level=logging.INFO)

def subQuery(sql_query, database_name="tutorial2_db"):
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
            c.city_name,
            s.name AS state_name,
            co.name AS country_name
        FROM people p
        JOIN cities c ON p.city_id = c.id
        JOIN states s ON c.state_id = s.id
        JOIN countries co ON s.country_id = co.id
        WHERE co.id = (
            SELECT id FROM countries WHERE name = 'Brazil'
        );
        """

subQuery(query, "tutorial2_db") 