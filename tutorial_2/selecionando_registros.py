import logging
logging.basicConfig(level=logging.INFO)

from mydb_connection import connect_to_db
from gen_people_fake_data import create_fake_people, create_cities


def records(database_name, table_name1, table_name2=None):
    conn = connect_to_db(database_name)
    if conn:
        cur = conn.cursor()
        # cur.execute(f"SELECT * FROM {table_name1} LIMIT 100")
        cur.execute(f"SELECT * FROM {table_name1} INNER JOIN {table_name2} ON {table_name1}.city_id = {table_name2}.id LIMIT 1000")  # INNER JOIN to combine data from both tables
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

# people_inserted_recors = records("tutorial2_db", "people")
cities_inserted_recors = records("tutorial2_db", "people", "cities")