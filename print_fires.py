import my_utils
import argparse
import sys


def print_fires(file_name, country_column, country, fires_column):

    """
    print_fires.py
    This function prints the number of fires in a specified country.

    Parameters:
        file_name (str): The name of the CSV file to read.
        country_column (int): Column index containing country names.
        country (str): The name of the country to search for.
        fires_column (int): Column index containing fire data.
    """

    try:
        fires = my_utils.get_column(file_name, country_column, country, fires_column)

        # Convert values in fires array to floats and sum; skip empty strings
        total_fires = sum(float(x) for x in fires if x.strip() != "")

        print(f'There were {total_fires} fires in {country}.')
        return total_fires
    
    except FileNotFoundError: 
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():    
    parser = argparse.ArgumentParser(description='Print the number of fires in a specified country from a CSV file.')
    parser.add_argument('--file_name', type=str, required=True, help='CSV file to read from.')
    parser.add_argument('--country_column', type=int, required=True, help='Column index for country names.')
    parser.add_argument('--country', type=str, required=True, help='The name of the country to search for.')
    parser.add_argument('--fires_column', type=int, required=True, help='Column index for fire data.')

    args = parser.parse_args()

    print_fires(args.file_name, args.country_column, args.country, args.fires_column)

if __name__ == "__main__":
    main()
