from mydb_connection import connect_to_db

conn = connect_to_db("tutorial2_db")
if conn:
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        age INTEGER,
        city_id INTEGER
    );
                
    CREATE TABLE IF NOT EXISTS cities (
        id SERIAL PRIMARY KEY,
        city_name VARCHAR(50),
        UF VARCHAR(2)
    );
    """)
    cur.close()
    conn.close()
else:
    print("Failed to connect to PostgreSQL.")