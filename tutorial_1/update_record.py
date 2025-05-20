from list_objects import list_tables
from reading_data import reading_tables_data
from database_conn import connect_to_university_db


def updateRecord(table_name, column_name, new_value, condition):
    """
    Update a record in the specified table.

    Args:
        table_name (str): The name of the table to update.
        column_name (str): The name of the column to update.
        new_value (str): The new value to set.
        condition (str): The condition to identify which record(s) to update.

    Returns:
        None
    """
    conn = connect_to_university_db() # Connect to the database university
    cursor = conn.cursor()

    # Construct the SQL UPDATE statement
    sql = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition}"
    cursor.execute(sql, (new_value,))

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()