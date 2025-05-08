from utils.gen_people_fake_data import create_fake_people, create_fake_courses

from database_conn import connect_to_university_db
import logging
logging.basicConfig(level=logging.INFO)


courses = create_fake_courses(12)

def insert_courses_data(courses_list):
    conn = connect_to_university_db()
    if conn:
        cur = conn.cursor()
        for course in courses_list:
            cur.execute("""
                INSERT INTO courses (course_name, teacher_id, description, start_date, end_date)
                VALUES (%s, %s, %s, %s, %s)
            """, (course['course_name'], course['teacher_id'], course['description'], course['start_date'], course['end_date']))
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

if __name__ == "__main__":
    insert_courses_data(courses)
    logging.info(f"{courses} Data inserted successfully.")