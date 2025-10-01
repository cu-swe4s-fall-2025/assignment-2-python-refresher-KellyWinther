import csv

input_file = "Agrofood_co2_emission.csv"
output_file = "test_data.csv"
target_country = "Australia"

with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Copy header
    header = next(reader)
    writer.writerow(header)

    # Copy rows only for Australia
    for row in reader:
        if row[0].strip() == target_country:
            writer.writerow(row)

print(f"Filtered data for {target_country} written to {output_file}")
