from postgres_connector import connect_to_postgres

def reading_tables_data(database_name, table_name):
    conn = connect_to_postgres(dbname=database_name)
    if conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")


reading_tables_data('university', 'people')