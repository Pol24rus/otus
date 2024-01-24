import csv
import json
from files_hw import CSV_FILE, CSV_TO_JSON_FILE_W

with open(CSV_FILE, newline='') as f:
    reader = csv.reader(f)
    array_dict = []
    # Извлекаем заголовок
    header = next(reader)[:4]
    header[2], header[3] = header[3], header[2]

    # Итерируемся по данным делая из них словари
    for row in reader:
        row[2], row[3] = row[3], row[2]
        csv_dict = dict(zip(header, row))  # делает словарь с ключом
        print('csv_dict ', csv_dict)
        array_dict.append(csv_dict)  # словарь книг
        print("full dictionary", array_dict)

with open(CSV_TO_JSON_FILE_W, "w") as f:
    s = json.dumps(array_dict, indent=4)
    f.write(s)

