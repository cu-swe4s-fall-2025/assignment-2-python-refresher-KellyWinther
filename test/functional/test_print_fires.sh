#!/bin/bash

#make executable (use once): chmod +x test/test_print_fires.sh

# Load ssshtest
test -e ssshtest || curl -s -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

source ssshtest

python="python3"
script="print_fires.py"
test_data="test/test_data.csv"


# no --operation for Australia prints list of fires
run test_no_operation $python $script \
    --file_name $test_data --country_column 0 --country Australia --fires_column 2
assert_in_stdout 54273 
assert_in_stdout 92588
assert_in_stdout 17618
assert_in_stdout 13405
assert_exit_code 0


# Operation tests
run test_mean $python $script \
    --file_name $test_data --country_column 0 --country Australia --fires_column 2 --operation mean
assert_in_stdout 44471

run test_median $python $script \
    --file_name $test_data --country_column 0 --country Australia --fires_column 2 --operation median
assert_in_stdout 17618

run test_stdev $python $script \
    --file_name $test_data --country_column 0 --country Australia --fires_column 2 --operation stdev
assert_in_stdout 27303


# Exit code/error tests
run test_no_file $python $script \
    --file_name non_file.csv --country_column 0 --country Australia --fires_column 2
assert_exit_code 1

run test_bad_column $python $script \
    --file_name $test_data --country_column 100 --country Australia --fires_column 2
assert_exit_code 1
