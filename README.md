[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)


# python-refresher and best practices homeworks: 

This repository contains the following:

In **src folder** 
- `my_utils.py` : get_columns function for extracting values from CSV files.
- `print_fires.py` : Command-line script for calculating fire counts by country.
- `run.sh` : Bash script to use of `print_fires.py`.

1. my_utils.py == this contains the get_columns function that reads a CSV line by line.  You must specify certain conditions. 
        -  What column you want to look for 
        -  What value you want to be true in that column 
        -  What new value in the cvs you care about reporting.  More details are in the my_utils.py. 


- Use the fucntion: 
```python
get_column(file_name, query_column, query_value, result_column=1)
``` 

2. print_fires.py == This script uses the get_columns function to search through a CSV to find the number of fires in a specified country and returns the list of integers representing the fires. 

**Parameters (command-line arguments):**
- `--file_name` : Name of the CSV file to read.
- `--country` : Country name to search for.
- `--country_column` : Index of the column where country names are stored.
- `--fires_column` : Index of the column containing fire values.

- Use the function: 
```bash
python3 print_fires.py  --country "United States of America"  --country_column 0  --fires_column 3  --file_name Agrofood_co2_emission.csv
```

3. run.sh == bash script which runs the python print_fires.py script. 

It includes:
1. A successful run (with correct arguments and file).
2. An argument error (missing required argument).
3. A file error (non-existent file).

- Use it: 
```bash
./run.sh
```


In **test folder**
1. test_data.csv == small set of 5 rows from every 10 years of Austrailia's reports (1990 to 2020)
2. test_my_utils.py == unit tests for the my_utils.py script. 
        - checks for positive and negative numbers and errors
3. test_print_fires.sh == uses ssshtest to test the print_fires.py script using the test_data.csv.
        - also tests the mean, median, and standard deviation (stdev) functions. 


**Continuous Integration:**
- Each time any branch pushes the workflow will automatically run unit, functional, and pycodestyle tests.

- Any time there is a pull from the main it will also automatically run unit, functional, and pycodestyle tests. 

1. unit test = test_my_utils.py
2. functional test = test_print_fires.sh
3. pycodestyle = uses pycode style to confirm that everything adheres to PEP8

- workflow testing is written in the "unit_test.yml" file in the .github/workflows folder