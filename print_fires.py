
import my_utils

#Identify file you want to read:
file_name = 'Agrofood_co2_emission.csv'


#Identify search parameters:
county_column = 0 #query_column = column index for country name
country='United States of America' #query_value = country of interest
#By default, result_column = 1 (the second column in the CSV), but you can change it to whatever column index you want.


#Options for result_column that report fires (please comment out the ones you don't want to run):
savanna_fires_column = 2 
forest_fires_column = 3  
organic_soil_fires_column = 24 
humid_tropical_forest_fires_column = 25 


#Run the function get_column to get the number of a given fire type in the specified country:
savanna_fires = my_utils.get_column(file_name, county_column, country, savanna_fires_column)
forest_fires = my_utils.get_column(file_name, county_column, country, forest_fires_column)
organic_soil_fires = my_utils.get_column(file_name, county_column, country, organic_soil_fires_column)
humid_tropical_forest_fires = my_utils.get_column(file_name, county_column, country, humid_tropical_forest_fires_column)


# Convert returned arrays to floats and sum; skipping empty strings
savanna_total = sum(float(x) for x in savanna_fires if x.strip() != "") 
forest_total = sum(float(x) for x in forest_fires if x.strip() != "")
organic_soil_total = sum(float(x) for x in organic_soil_fires if x.strip() != "")
humid_tropical_forest_total = sum(float(x) for x in humid_tropical_forest_fires if x.strip() != "")

Total_fires = savanna_total + forest_total + organic_soil_total + humid_tropical_forest_total


print(f'There were {savanna_total} savanna fires in {country}.')
print(f'There were {forest_total} forest fires in {country}.')
print(f'There were {organic_soil_total} organic soil fires in {country}.')
print(f'There were {humid_tropical_forest_total} humid tropical forest fires in {country}.')
print(f'There were {Total_fires} total fires in {country}.')
