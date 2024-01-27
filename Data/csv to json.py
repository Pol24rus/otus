import csv
import json
from files_hw import JSON_FILE, CSV_FILE_W, CSV_FILE
json_file_path = 'output.json'  # Replace with the desired output JSON file path

with open(CSV_FILE, newline='') as f2:
    reader = csv.reader(f2)
    array_dict = []
    # Извлекаем заголовок
    header = next(reader)[:4]
    header[2], header[3] = header[3], header[2]
    # Итерируемся по данным делая из них словари
    for row in reader:
        row[2], row[3] = row[3], row[2]
        csv_dict = dict(zip(header, row))  # делает словарь с ключом
        #        print('csv_dict ',csv_dict)
        array_dict.append(csv_dict)  # словарь книг


with open(CSV_FILE_W, "w") as f3:
    s = json.dumps(array_dict, indent=4)
    f3.write(s)