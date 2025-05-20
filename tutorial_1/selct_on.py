from list_objects import list_tables
from reading_data import reading_tables_data
from database_conn import connect_to_university_db


def getRecord(table_name, condition):
    """
    Retrieve a record from the specified table.

    Args:
        table_name (str): The name of the table to retrieve from.
        condition (str): The condition to identify which record(s) to retrieve.

    Returns:
        list: A list of records that match the condition.
    """
    conn = connect_to_university_db()  # Connect to the database university
    cursor = conn.cursor()

    # Construct the SQL SELECT statement
    sql = f"SELECT * FROM {table_name} WHERE {condition}"
    cursor.execute(sql)

    # Fetch all matching records
    records = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    return records