import os
import logging
import csv
from gen_people_fake_data import *


logging.basicConfig(level=logging.INFO)

def write_csv_file(file_name, dataframe):
    try:
        if dataframe:
            with open(file_name, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=dataframe[0].keys())
                writer.writeheader()
                writer.writerows(dataframe)
    except Exception as e:
        logging.error(f"Error writing to file {file_name}: {e}")


if __name__ == "__main__":
    people_1 = create_fake_people(1000, start_id=1)
    people_2 = create_fake_people(250, start_id=1001)

    countries = create_countries(1)
    states = create_states(28)
    cities = create_cities(112)
    addresses = create_addresses(112)

    # write_csv_file('tutorial_2/files/people_1.csv', people_1)
    # write_csv_file('tutorial_2/files/people_2.csv', people_2)

    # write_csv_file('tutorial_2/files/countries.csv', countries)
    # write_csv_file('tutorial_2/files/states.csv', states)
    # write_csv_file('tutorial_2/files/cities.csv', cities)
    write_csv_file('tutorial_2/files/addresses.csv', addresses)
