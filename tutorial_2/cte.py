
import logging
from mydb_connection import connect_to_db

logging.basicConfig(level=logging.INFO)

def CTE(sql_query, database_name="tutorial2_db"):
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
        WITH PeopleCountPerCity AS (
                                    SELECT
                                            c.city_name,
                                            COUNT(p.id) AS people_count
                                        FROM people p
                                        JOIN cities c ON p.city_id = c.id
                                        GROUP BY c.city_name
                                    )
                                    SELECT
                                        city_name,
                                        people_count
                                    FROM PeopleCountPerCity
                                    WHERE people_count > 1
                                    ORDER BY people_count DESC;
        """

CTE(query, "tutorial2_db") 