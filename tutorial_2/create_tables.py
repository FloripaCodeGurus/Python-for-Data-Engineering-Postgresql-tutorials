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
        CREATE TABLE IF NOT EXISTS phones (
            id SERIAL PRIMARY KEY,
            phone_number TEXT NOT NULL,
            person_id INT NOT NULL REFERENCES people(id)
        );
        CREATE TABLE IF NOT EXISTS stores (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            country_id INT NOT NULL REFERENCES countries(id),
            state_id INT NOT NULL REFERENCES states(id),     
            city_id INT NOT NULL REFERENCES cities(id),
            address_id INT NOT NULL REFERENCES addresses(id)
        );
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            stock INTEGER NOT NULL,
            store_id INT NOT NULL REFERENCES stores(id)
        );             
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            person_id INT NOT NULL REFERENCES people(id),
            total_amount NUMERIC(10, 2) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS order_items (
            id SERIAL PRIMARY KEY,
            order_id INT NOT NULL REFERENCES orders(id),
            product_id INT NOT NULL REFERENCES products(id),
            quantity INTEGER NOT NULL,
            price NUMERIC(10, 2) NOT NULL
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

if __name__ == "__main__":
    create_tables()
    logging.info("Tables created successfully.")