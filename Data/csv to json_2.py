import csv
import json
from csv import DictReader
from files_hw import CSV_FILE, CSV_TO_JSON_FILE_W

with open(CSV_FILE, newline='') as f:
    reader = DictReader(f)
    array_dict = []

    # Итерируемся по данным делая из них словари
    for row in reader:
        array_dict.append(row)  # словарь книг

with open(CSV_TO_JSON_FILE_W, "w") as f:
    s = json.dumps(array_dict, indent=4)
    f.write(s)