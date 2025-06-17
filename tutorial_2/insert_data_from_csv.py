
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


def insert_people_data():
    try:
        dataset = 'people_1'
        table_name = 'people'
        csv_file_path = f"tutorial_2/files/{dataset}.csv"
        data = read_csv_file(csv_file_path)
        if data:
            query = f"INSERT INTO {table_name} (id,first_name,last_name,age,city_id) VALUES (%s, %s, %s, %s, %s)"
            for row in data:
                values = (int(row["id"]), row["first_name"], row["last_name"], row["age"], row["city_id"] )
                insert_data_from_csv("tutorial2_db", query, values)
            logging.info(f"Data inserted successfully into table {dataset}.")
        else:
            logging.info("No data to insert.")
    except Exception as e:
        logging.error(f"Error inserting people data: {e}")


def insert_country_data():
    try:
        dataset = 'countries'
        table_name = 'countries'
        csv_file_path = f"tutorial_2/files/{dataset}.csv"
        data = read_csv_file(csv_file_path)
        if data:
            query = f"INSERT INTO {table_name} (id,name) VALUES (%s, %s)"
            for row in data:
                values = (int(row["id"]), row["name"])
                insert_data_from_csv("tutorial2_db", query, values)
            logging.info(f"Data inserted successfully into table {dataset}.")
        else:
            logging.info("No data to insert.")
    except Exception as e:
        logging.error(f"Error inserting people data: {e}")


def insert_states_data():
    try:
        dataset = 'states'
        table_name = 'states'
        csv_file_path = f"tutorial_2/files/{dataset}.csv"
        data = read_csv_file(csv_file_path)
        if data:
            query = f"INSERT INTO {table_name} (id, name, uf, country_id) VALUES (%s, %s, %s,%s)"
            for row in data:
                values = (int(row["id"]), row["name"], row["uf"], 1) # fixed country_id for Brazil (1)
                insert_data_from_csv("tutorial2_db", query, values)
            logging.info(f"Data inserted successfully into table {dataset}.")
        else:
            logging.info("No data to insert.")
    except Exception as e:
        logging.error(f"Error inserting people data: {e}")

def insert_cities_data():
    try:
        dataset = 'cities'
        table_name = 'cities'
        csv_file_path = f"tutorial_2/files/{dataset}.csv"
        data = read_csv_file(csv_file_path)
        if data:
            query = f"INSERT INTO {table_name} (id, city_name, state_id) VALUES (%s, %s,%s)"
            for row in data:
                values = (int(row["id"]), row["city_name"], row["state_id"])
                insert_data_from_csv("tutorial2_db", query, values)
            logging.info(f"Data inserted successfully into table {dataset}.")
        else:
            logging.info("No data to insert.")
    except Exception as e:
        logging.error(f"Error inserting people data: {e}")

def insert_addresses_data():
    try:
        dataset = 'addresses'
        table_name = 'addresses'
        csv_file_path = f"tutorial_2/files/{dataset}.csv"
        data = read_csv_file(csv_file_path)
        if data:
            query = f"INSERT INTO {table_name} (id, street, number, city_id) VALUES (%s, %s,%s, %s)"
            for row in data:
                values = (int(row["id"]), row["street"], row["number"], row["city_id"])
                insert_data_from_csv("tutorial2_db", query, values)
            logging.info(f"Data inserted successfully into table {dataset}.")
        else:
            logging.info("No data to insert.")
    except Exception as e:
        logging.error(f"Error inserting people data: {e}")


if __name__ == "__main__":
    # insert_people_data()
    # insert_country_data()
    # insert_states_data()
    # insert_cities_data()
    insert_addresses_data()

