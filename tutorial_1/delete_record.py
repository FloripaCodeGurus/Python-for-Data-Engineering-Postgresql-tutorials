from list_objects import list_tables
from reading_data import reading_tables_data
from database_conn import connect_to_university_db



def deleteRecord(table_name, condition):
    """
    Delete a record from the specified table.

    Args:
        table_name (str): The name of the table to delete from.
        condition (str): The condition to identify which record(s) to delete.

    Returns:
        None
    """
    conn = connect_to_university_db() # Connect to the database university
    cursor = conn.cursor()

    # Construct the SQL DELETE statement
    sql = f"DELETE FROM {table_name} WHERE {condition}"
    cursor.execute(sql)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()