import logging
from mydb_connection import connect_to_db

logging.basicConfig(level=logging.INFO)
def create_tables():
    try:
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
                
            CREATE TABLE IF NOT EXISTS people_for_union (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INTEGER,
                city_id INTEGER
            );
            
                
           CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
            );

                
           CREATE TABLE IF NOT EXISTS states (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            uf CHAR(2) NOT NULL,
            country_id INT NOT NULL REFERENCES countries(id)
            );
                
            CREATE TABLE IF NOT EXISTS cities (
            id SERIAL PRIMARY KEY,
            city_name TEXT NOT NULL,
            state_id INT NOT NULL REFERENCES states(id)
            );


            CREATE TABLE IF NOT EXISTS addresses (
            id SERIAL PRIMARY KEY,
            street TEXT NOT NULL,
            number TEXT NOT NULL,
            city_id INT NOT NULL REFERENCES cities(id)
        );

        """)
            cur.close()
            conn.commit()
        else:
            logging.error("Failed to connect to PostgreSQL.")
    except Exception as e:
        logging.error(f"Error creating tables: {e}")
    finally:
        if conn:
            conn.close()