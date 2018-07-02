import os, sys
import csv, json

if __name__ == "__main__":
	# Check if user has input a file path
	if len(sys.argv) == 1:
		print("Invalid number of arguments")
		sys.exit()

	# Input file path of the csv file
	input_file_path = sys.argv[1]

	# Output file path of the json file
	output_file_path = sys.argv[2]

	# Open csv file
	with open(input_file_path, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		with open(output_file_path, 'w') as json_file:
			json_output = json.dumps(list(csv_reader))
			json_file.write(json_output)
		