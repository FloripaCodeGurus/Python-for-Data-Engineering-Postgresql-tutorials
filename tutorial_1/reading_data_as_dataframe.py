import pandas as pd
from database_conn import connect_to_university_db


def read_table_as_dataframe(table_name) -> pd.DataFrame:
    """
    Reads a table from the database and returns it as a pandas DataFrame.
    """
    engine = connect_to_university_db()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, con=engine)
    return df

if __name__ == "__main__":
    # Principais informações sobre a tabela people
    print()
    people_df = read_table_as_dataframe('people')
    print("==================================================================================")
    print(f"Numero de registros: {len(people_df)}")
    print("==================================================================================")
    print("Colunas")
    print(people_df.columns)
    print("==================================================================================")
    print("Primeiros 5 registros")
    print(people_df.head())
    print("==================================================================================")
    print("Ultimos 5 registros")
    print(people_df.tail())
    print("==================================================================================")
    print(f"Tipo de dados: {people_df.dtypes}")
    print("==================================================================================")
    print(f"Informações: {people_df.info()}")
    print("==================================================================================")
    print(f"Estatísticas: {people_df.describe()}")
    print("==================================================================================")
    print(f"Valores nulos: {people_df.isnull().sum()}")