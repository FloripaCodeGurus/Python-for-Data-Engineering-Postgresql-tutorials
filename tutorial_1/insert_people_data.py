from utils.gen_people_fake_data import create_fake_people
from database_conn import connect_to_university_db
import logging
logging.basicConfig(level=logging.INFO)

students = create_fake_people(5000, role="student")
techers = create_fake_people(50, role="teacher")
principals = create_fake_people(1, role="principal")
supervisors = create_fake_people(40, role="supervisor")


# for super in  supervisors:
#     print(super)

def insert_people_data(people_list):
    conn = connect_to_university_db()
    if conn:
        cur = conn.cursor()
        for person in people_list:
            cur.execute("""
                INSERT INTO people (first_name, last_name, role, age, phone_number, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (person['first_name'], person['last_name'], person['role'], person['age'], person['phone_number'], person['email']))
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

if __name__ == "__main__":
    insert_people_data(supervisors)
    logging.info(f"{supervisors} Data inserted successfully.")

    insert_people_data(students)
    logging.info(f"{students} Data inserted successfully.")

    insert_people_data(techers)
    logging.info(f"{techers} Data inserted successfully.")

    insert_people_data(principals)
    logging.info(f"{principals} Data inserted successfully.")