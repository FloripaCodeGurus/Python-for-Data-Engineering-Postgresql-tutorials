from utils.gen_people_fake_data import create_fake_people, create_fake_courses, evaluation_test
from database_conn import connect_to_university_db
from list_objects import list_tables

import logging
logging.basicConfig(level=logging.INFO)


def test_results(evaluation_test):
    conn = connect_to_university_db()
    if conn:
        cur = conn.cursor()
        for course in evaluation_test:
            cur.execute("""
                INSERT INTO courses (discipline, teacher_id, teacher_first_name, teacher_last_name, student, grade, test_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (course['discipline'], 
                  course['teacher_id'], 
                  course['teacher_first_name'], 
                  course['teacher_last_name'], 
                  course['student']),
                  course['grade'],
                  course['test_date'],
                  )
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

if __name__ == "__main__":
    test_results("Matematica")
    logging.info(f"Data inserted successfully.")