
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



def insert_people_2_data(): # use country_id from coutries.csv or coutries table
    dataset = 'people_2'
    table_name = 'people_for_union'
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


def create_union_fuction(table_name1, table_name2, union_type):
    try:
        conn = connect_to_db("tutorial2_db")
        if conn:
            cur = conn.cursor()
            cur.execute(f"""SELECT * FROM {table_name1} {union_type} SELECT * FROM {table_name2}""")
            union_data = cur.fetchall()
            print(f"Union Data registers :{len(union_data)}")
            cur.close()
            conn.commit()
        else:
            logging.error("Failed to connect to PostgreSQL.")
    except Exception as e:
        logging.error(f"Error creating tables: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # insert_people_2_data()
    create_union_fuction("people", "people_for_union", union_type="UNION")
    create_union_fuction("people", "people_for_union", union_type="UNION ALL")

