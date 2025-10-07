import my_utils
import argparse
import sys


def print_fires(file_name,
                country_column,
                country,
                fires_column,
                operation=None):

    """
    print_fires.py
    This function prints the number of fires in a specified country.

    Parameters:
        file_name (str): The name of the CSV file to read.
        country_column (int): Column index for country names.
        country (str): The name of the country to search for.
        fires_column (int): Column index for fire data.
    """

    try:
        fires = my_utils.get_column(file_name,
                                    country_column,
                                    country,
                                    fires_column)

    # Convert values in fires array to floats then integers; skip empty strings
        fires_list = [int(float(x)) for x in fires if x != '']

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    return fires_list


def main():
    parser = argparse.ArgumentParser(
        description='Print the number of fires in a specified country from a CSV file.')
    
    parser.add_argument('--file_name',
                        type=str,
                        required=True,
                        help='CSV file to read from.')
    
    parser.add_argument('--country_column',
                        type=int,
                        required=True,
                        help='Column index for country names.')

    parser.add_argument('--country',
                        type=str,
                        required=True,
                        help='The name of the country to search for.')

    parser.add_argument('--fires_column',
                        type=int,
                        required=True,
                        help='Column index for fire data.')

    parser.add_argument('--operation',
                        type=str,
                        choices=['mean', 'median', 'stdev'],
                        help='Optional: Perform mean, median, or stdev on the returned fire values.')

    args = parser.parse_args()

    all_fires = print_fires(args.file_name,
                            args.country_column,
                            args.country,
                            args.fires_column,
                            args.operation)

    if args.operation == 'mean':
        result = int(my_utils.mean(all_fires))
        print(f"The mean number of fires in {args.country} is {result}.")
    elif args.operation == 'median':
        result = int(my_utils.median(all_fires))
        print(f"The median number of fires in {args.country} is {result}.")
    elif args.operation == 'stdev':
        result = int(my_utils.stdev(all_fires))
        print(f"The standard deviation of fires in {args.country} is {result}.")
    else:
        print(f"There were {all_fires} fires in {args.country}.")

    return all_fires


if __name__ == "__main__":
    main()
