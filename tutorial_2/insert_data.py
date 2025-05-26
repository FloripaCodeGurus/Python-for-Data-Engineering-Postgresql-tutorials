import logging
logging.basicConfig(level=logging.INFO)

from mydb_connection import connect_to_db
from gen_people_fake_data import create_fake_people, create_cities




def insert_records(database_name, query, values):
    conn = connect_to_db(database_name)
    if conn:
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

def insert_cities_data():
    try:
        cities = create_cities(1248)
        for city in cities:
            # print(city)
            query = "INSERT INTO cities (id, city_name, UF) VALUES (%s, %s, %s)"
            values = (city["id"], city["city_name"], city["UF"])
            insert_records("tutorial2_db", query, values)
        logging.info(f"Data inserted successfully on table cities.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")

def insert_people_data():
    try:
        people = create_fake_people(5248)
        for p in people:
            # print(city)
            query = "INSERT INTO people (id, first_name, last_name, age, city_id) VALUES (%s, %s, %s, %s, %s)"
            values = (p["id"], p["first_name"], p["last_name"], p["age"], p["city_id"])
            insert_records("tutorial2_db", query, values)
        logging.info(f"Data inserted successfully on table people.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")


if __name__ == "__main__":
    # cities = create_cities(1248)
    insert_people = insert_people_data()