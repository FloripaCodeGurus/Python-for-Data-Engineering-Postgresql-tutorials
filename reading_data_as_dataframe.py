import pandas



def read_table_as_dataframe(file_path: str) -> pandas.DataFrame:
    """
    Reads a table from a file and returns it as a pandas DataFrame.
    
    Args:
        file_path (str): The path to the file containing the table.
        
    Returns:
        pandas.DataFrame: The table as a pandas DataFrame.
    """
    # Read the table from the file
    df = pandas.read_table(file_path, sep="\t")
    
    return df

