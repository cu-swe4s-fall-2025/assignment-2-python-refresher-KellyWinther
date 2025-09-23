import sys


def get_column(file_name, query_column, query_value, result_column=1):

    """
    This function reads a CSV file and retrieves values from a specified column.

    Parameters:
    - file_name (str): Name of the CSV file to read.
    - query_column (int): Index of the column that you want to search for specific values.
    - query_value (str): Value to search for in the specified query_column.
    - result_column (int): Index of the column you want to retrieve new values. Default is 1.

    Returns:
    - List of integers: Values from result_column where the query_column == query_value.
    """

    # Initialize an empty array to store results
    results = []

    # Open the file and read line by line:
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split(",")
            
            # check if the value in the query_column matches the query_value
            if values[query_column] == (query_value):
                try:
                    # convert to integers and append to results array if its a match
                    results.append(int(float(values[result_column])))

                except ValueError:
                    print (f"Cannot convert value '{values[result_column]}'")
                    sys.exit(1)

    return results
