from postgres_connector import connect_to_postgres

def list_databases():
    conn = connect_to_postgres()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = cur.fetchall()
        print("Databases:")
        for db in databases:
            print(f"- {db[0]}")
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

def list_tables(database_name):
    conn = connect_to_postgres(dbname=database_name)
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cur.fetchall()
        print(f"Tables in database '{database_name}':")
        for table in tables:
            print(f"- {table[0]}")
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

# Example usage:
list_databases()
list_tables('university')