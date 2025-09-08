
import my_utils

#Identify file you want to read:
file_name = 'Agrofood_co2_emission.csv'

#Identify search parameters:
county_column = 0 #query_column = column index for country name
country='Jordan' #query_value = country of interest
fires_column = 3 #result_column = column indext for forest fires

#Run the function get_column to get the number of forest fires in the specified country:
fires = my_utils.get_column(file_name, county_column, country, fires_column)

print(f'Across different years of reports, there were {fires} forest fires in {country}.')
