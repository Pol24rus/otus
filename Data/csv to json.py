import csv
import json

from csv import DictReader
from files_hw import CSV_FILE
# csv_file_path = 'input.csv'  # Replace with your CSV file path
json_file_path = 'output.json'  # Replace with the desired output JSON file path


# Step 1: Open the CSV file and convert it to a JSON file
def csv_to_json(CSV_FILE, json_file_path):
    data = {}
    with open(CSV_FILE, encoding='utf-8') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)[:4]
        header[2], header[3] = header[3], header[2]
        for rows in csv_reader:
            rows[2], rows[3] = rows[3], rows[2]
            keys = rows[0]  # Assuming a column named 'Serial Number' as the primary key
            data[keys] = rows[:4]

            # key = rows['Book']  # Assuming a column named 'Serial Number' as the primary key
            # data[key] = rows
            csv_dict = dict(zip(header, rows))
            print("row", csv_dict)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data[header], data[rows], indent=4))


# Step 2: Call the function with the file paths
csv_to_json(CSV_FILE, json_file_path)
