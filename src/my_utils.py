import sys


def get_column(file_name, query_column, query_value, result_column=1):

    """
    Read a CSV file and retrieve values from a specified column.

    Parameters:
    - file_name (str): Name of the CSV file to read.
    - query_column (int): Index of column to search within.
    - query_value (str): Value to search for in the specified query_column.
    - result_column (int): Index of column to retrieve values. Default: 1

    Returns:
    - List (int): result_column values when query_column == query_value.
    """

    # Initialize an empty array to store results
    results = []

    # Open the file and read line by line:
    try:
        with open(file_name, "r") as file:
            for line in file:
                values = line.strip().split(",")

                # does the query_column matches the query_value?
                if values[query_column] == (query_value):
                    try:
                        # convert to integer and append to results array
                        results.append(int(float(values[result_column])))

                    except ValueError:
                        print(f"Cannot convert: '{values[result_column]}'")
                        sys.exit(1)

    except FileNotFoundError:
        print(f"Error: File not found: {file_name}")
        sys.exit(1)

    except IndexError:
        print("Error: query_column or result_column out of bounds")
        sys.exit(1)

    return results


def mean(int_array):
    '''
    Return the mean value for a given array of numbers as a float.

    Parameters:
    - int_array (list):Array of numbers to calculate the mean from.

    Returns:
    - mean_value (float): Mean value of the array.
    '''

    try:
        mean_value = sum(int_array) / len(int_array)

    except ZeroDivisionError:
        print("Error: Cannot calculate mean of an empty array")
        sys.exit(1)

    return mean_value


def median(int_array):
    '''
    Find the median value of an array of numbers.

    Parameters:
    - int_array (list):list of numbers (does not need to be pre-sorted).

    Returns:
    - median_value (float): The median value.
    '''

    try:
        sorted_array = sorted(int_array)
        n = len(sorted_array)
        mid = n // 2

        if n % 2:  # odd
            median_value = sorted_array[mid]
        else:      # even
            median_value = (sorted_array[mid - 1] + sorted_array[mid]) / 2

    except IndexError:
        print("Error: Cannot calculate median of an empty array")
        sys.exit(1)

    return median_value


def stdev(array):
    '''
    This function finds the standard deviation of an array of integers.

    Parameters:
    array (list): A list of integers to find the standard deviation of.

    Returns:
    std (float): The standard deviation of the array.
    '''
    try:
        array_mean = mean(array)
        residual_sum = 0

        for value in array:
            residual_sum += (value - array_mean) ** 2
        std = (residual_sum / len(array)) ** 0.5

    except ZeroDivisionError:
        print("Error: Cannot calculate standard deviation of an empty array")
        sys.exit(1)

    return std
