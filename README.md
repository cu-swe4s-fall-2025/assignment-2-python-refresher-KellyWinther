[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

1. my_utils.py == this is a function that can take a CSV and read it line by line to find specific values in the CSV.  You must specify certain conditions. (1) What column you want to look for (2) what value you want to be true in that column (3) what new value in the cvs you care about reporting.  More details are in the my_utils.py. 
        Use the fucntion: get_column(file_name, query_column, query_value, result_column)
        * the default result column is index = 1 


2. print_fires == If using the Agro_co2_emission.csv: This script uses the get_columns function to find the number of fires in a specified country and prints out the sum of all fires by type of fire as well as the total of all fire types combined. Note: this data is limited to the years that were reported and not all countries are reported equally. 

3. run.sh == bash script which runs the python print_fires.py script. Right now it is set to United States of America, but you can edit the print_fires.py script to pick a different country. 

