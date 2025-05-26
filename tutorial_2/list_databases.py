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


if __name__ == "__main__":
    list_databases()
