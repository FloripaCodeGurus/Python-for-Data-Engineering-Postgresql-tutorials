
import logging
import csv
from mydb_connection import connect_to_db

logging.basicConfig(level=logging.INFO)

def read_csv_file(csv_file_path):
    try:
        with open(csv_file_path, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        logging.info(f"Error reading CSV file: {e}")
        return None
    

def insert_data_from_csv(database_name, query, values):
    try:
        conn = connect_to_db(database_name)
        if conn:
            cur = conn.cursor()
            cur.execute(query, values)
            conn.commit()
            cur.close()
            conn.close()
        else:
            logging.info("Failed to connect to PostgreSQL.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")

states_ids = list(range(1, 29))
cities_ids = list(range(1, 113))


def insert_states_data(): # use country_id from coutries.csv or coutries table
    dataset = 'states'
    csv_file_path = f"tutorial_2/files/{dataset}.csv"
    data = read_csv_file(csv_file_path)
    if data:
        query = f"INSERT INTO {dataset} (id, state_name, coutry_id) VALUES (%s, %s, %s)"
        for row in data:
            values = (int(row["id"]), row["state_name"])
            insert_data_from_csv("tutorial2_db", query, values)
        logging.info(f"Data inserted successfully into table {dataset}.")
    else:
        logging.info("No data to insert.")

def insert_cities_data():  # use states_ids from states.csv or states table
    dataset = 'cities'
    csv_file_path = f"tutorial_2/files/{dataset}.csv"
    data = read_csv_file(csv_file_path)
    if data:
        query = f"INSERT INTO {dataset} (id, city_name, state_id) VALUES (%s, %s, %s)"
        for row in data:
            values = (int(row["id"]), row["city_name"], int(row["state_id"]))
            insert_data_from_csv("tutorial2_db", query, values)
        logging.info(f"Data inserted successfully into table {dataset}.")
    else:
        logging.info("No data to insert.")

def insert_address_data(): #  # use cities_ids from cities.csv or cities table
    dataset = 'addresses'
    csv_file_path = f"tutorial_2/files/{dataset}.csv"
    data = read_csv_file(csv_file_path)
    if data:
        existing_city_ids = get_existing_state_ids("tutorial2_db", "cities")
        used_city_ids = set()
        valid_rows = []
        for row in data:
            original_city_id = int(row["city_id"])
            city_id = original_city_id
            # Increment city_id until it's unique in this batch and exists in cities table
            while city_id in used_city_ids or city_id not in existing_city_ids:
                city_id += 1
            used_city_ids.add(city_id)
            # Update the row with the new city_id
            row["city_id"] = city_id
            valid_rows.append(row)
        if valid_rows:
            query = f"INSERT INTO {dataset} (id,street,number,city_id) VALUES (%s, %s, %s, %s)"
            for row in valid_rows:
                values = (int(row["id"]), row["street"], int(row["number"]), int(row["city_id"]))
                insert_data_from_csv("tutorial2_db", query, values)
            logging.info(f"Inserted {len(valid_rows)} addresses with unique city_id(s).")
        else:
            logging.info("No valid addresses to insert.")
    else:
        logging.info("No data to insert.")

if __name__ == "__main__":
    # insert_missing_states(missing_states_ids)
    # insert_cities_data()
    insert_address_data()

