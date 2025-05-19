from database_conn import connect_to_university_db

conn = connect_to_university_db()
if conn:
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        role VARCHAR(50),
        age INTEGER,
        phone_number VARCHAR(30),
        email VARCHAR(100),
        gender VARCHAR(10)
    );
    CREATE TABLE IF NOT EXISTS courses (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(100),
        teacher_id INTEGER REFERENCES people(id),
        description TEXT,
        start_date DATE,
        end_date DATE
    );
    CREATE TABLE IF NOT EXISTS grades (
        PRIMARY KEY (student_id, course_id),
        student_id INTEGER REFERENCES people(id),
        course_id INTEGER REFERENCES courses(id),
        grade FLOAT,
        date DATE
    );
    CREATE TABLE IF NOT EXISTS classes (
        id SERIAL PRIMARY KEY,
        course_id INTEGER REFERENCES courses(id),
        start_time TIME,
        end_time TIME,
        day_of_week VARCHAR(10)
    );
                
    CREATE TABLE IF NOT EXISTS evaluation_test (
        id SERIAL PRIMARY KEY,
        discipline VARCHAR(100),
        teacher_id INTEGER REFERENCES people(id),
        teacher_first_name VARCHAR(50),
        teacher_last_name VARCHAR(50),
        student JSONB,
        grade FLOAT,
        test_date DATE
    );
    """)
    cur.close()
    conn.close()
else:
    print("Failed to connect to PostgreSQL.")