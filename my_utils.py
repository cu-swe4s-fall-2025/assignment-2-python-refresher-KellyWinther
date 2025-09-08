def get_column(file_name, query_column, query_value, result_column):

#   This function reads a CSV file and retrieves values from a specified column:
#   - file_name: Name of the CSV file to read.
#   - query_column: Index of the column that you want to search for specific values.
#   - query_value: Value to search for in the specified query_column.
#   - result_column: Index of the column you want to retrieve new values when a match between query_column and query_value is TRUE

#Initialize an empty list/array to store results
    results = []

#Open the file and read line by line:
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split(",")

            if values[query_column] == (query_value): #check if the value in the query_column matches the query_value
                results.append(values[result_column]) #If it matches, save the value from the result_column into the results list/array

    return results
