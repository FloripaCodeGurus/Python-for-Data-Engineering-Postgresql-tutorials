import os
import logging
from gen_people_fake_data import *


logging.basicConfig(level=logging.INFO)

def write_csv_file(file_name, dataframe):
    try:
        with open(file_name, 'w') as f:
            if dataframe:
                # Write header
                header = ','.join(dataframe[0].keys())
                f.write(header + '\n')
                # Write data rows
                for row in dataframe:
                    line = ','.join(str(value) for value in row.values())
                    f.write(line + '\n')
    except Exception as e:
        logging.error(f"Error writing to file {file_name}: {e}")


if __name__ == "__main__":
    people_1 = create_fake_people(1000, start_id=1)
    people_2 = create_fake_people(250, start_id=1001)

    cities = create_cities(10)

    write_csv_file('tutorial_2/files/people_1.csv', people_1)
    write_csv_file('tutorial_2/files/people_2.csv', people_2)
    write_csv_file('tutorial_2/files/cities.csv', cities)