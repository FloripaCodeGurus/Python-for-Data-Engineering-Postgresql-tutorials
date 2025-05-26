import logging
logging.basicConfig(level=logging.INFO)

from mydb_connection import connect_to_db


def groupData(database_name, table_name1, table_name2=None, grouped_record=None, tb_filed_1=None, tb_filed_2=None):
    conn = connect_to_db(database_name)
    if conn:
        cur = conn.cursor()
        query = F"""SELECT {table_name2}.{grouped_record}, COUNT({table_name1}.{tb_filed_1}) AS {table_name1} FROM {table_name2} INNER JOIN 
                    {table_name1} ON {table_name2}.{tb_filed_2} = {table_name1}.{tb_filed_1} GROUP BY {table_name2}.{grouped_record};"""
        print(query)
        cur.execute(query) 
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")

table_name1= "people"
table_name2= "cities"
tb_filed_1= "city_id"
tb_filed_2= "id"
grouped_record = "city_name"
grouped_by_data = groupData("tutorial2_db", table_name1, table_name2, grouped_record, tb_filed_1, tb_filed_2)

# QUERY EXECUTADA
"""SELECT cities.city, COUNT(people.city_id) AS persons
FROM cities INNER JOIN people ON cities.id = people.city_id
GROUP BY cities.city_name;"""