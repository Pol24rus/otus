import json
import csv
from files_hw import JSON_FILE, JSON_FILE_W, CSV_FILE
from csv import DictReader

result = []

with open(JSON_FILE, "r") as f:
    users = json.load(f)
    user_number = 0
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "Book": []})
        user_number += 1

with open(CSV_FILE, newline='') as f2:
    reader = DictReader(f2)
    array_dict = []
    # Итерируемся по данным делая из них словари
    for row in reader:
        array_dict.append(row)  # словарь книг


with open(JSON_FILE_W, "w") as f3:
    s = json.dumps(array_dict, indent=4)
    f3.write(s)
