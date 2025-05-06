from postgres_connector import connect_to_postgres

conn = connect_to_postgres()
if conn:
    cur = conn.cursor()
    cur.execute("CREATE DATABASE university;")
    cur.close()
    conn.close()
else:
    print("Failed to connect to PostgreSQL.")

