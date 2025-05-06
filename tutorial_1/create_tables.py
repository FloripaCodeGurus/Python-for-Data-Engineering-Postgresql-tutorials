from database_conn import connect_to_university_db

conn = connect_to_university_db()
if conn:
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE people (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        role VARCHAR(50),
        age INTEGER,
        phone_number VARCHAR(15),
        email VARCHAR(100),
        gender VARCHAR(10)
    );
    CREATE TABLE courses (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(100),
        teacher_id INTEGER REFERENCES people(id),
        description TEXT,
        start_date DATE,
        end_date DATE
    );
    CREATE TABLE grades (
        PRIMARY KEY (student_id, course_id),
        student_id INTEGER REFERENCES people(id),
        course_id INTEGER REFERENCES courses(id),
        grade FLOAT,
        date DATE
    );
    CREATE TABLE classes (
        id SERIAL PRIMARY KEY,
        course_id INTEGER REFERENCES courses(id),
        start_time TIME,
        end_time TIME,
        day_of_week VARCHAR(10)
    );
""")
    cur.close()
    conn.close()
else:
    print("Failed to connect to PostgreSQL.")