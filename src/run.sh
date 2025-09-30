#!/bin/bash

# This script runs a Python program that reports the number of fires in the specified country.
# It uses the 'my_utils.py' function 'get_column' to read data from a CSV file.

# make sure to give execute permissions with: chmod +x run.sh
# then run with: ./run.sh

# Example 1 - successful run
echo "-- Example of a successful run --"
python3 print_fires.py \
    --file_name "Agrofood_co2_emission.csv" \
    --country_column 0 \
    --country "United States of America" \
    --fires_column 2
    

#Example 2 - unsuccessful run (missing country_column)
echo "-- Example of an unsuccessful run (missing country_column) --"
python3 print_fires.py \
   --file_name "Agrofood_co2_emission.csv" \
   --country "United States of America" \
   --fires_column 2 
    

#Example 3 - unsuccessful run (file not found)
echo "-- Example of an unsuccessful run (file not found) --"
python3 print_fires.py \
   --file_name "I_do_not_exist.csv" \
   --country_column 0 \
   --country "United States of America" \
   --fires_column 2 
    