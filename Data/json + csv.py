import json
import csv
from files_hw import JSON_FILE, JSON_FILE_W
from files_hw import CSV_FILE

result = []

with open(JSON_FILE, "r") as f:
    users = json.load(f)
    user_number = 0
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "Book": []})
        user_number += 1

with open(CSV_FILE, newline='') as f:
    reader = csv.reader(f)
    array_dict = []
    # Извлекаем заголовок
    header = next(reader)[:4]
    header[2],header[3] = header[3],header[2]
    # Итерируемся по данным делая из них словари
    for row in reader:
        row[2],row[3] = row[3],row[2]
        csv_dict = dict(zip(header, row)) # делает словарь с ключом
        print('csv_dict ',csv_dict)
        array_dict.append(csv_dict) # словарь книг
        print("full dictionary", array_dict)

with open(JSON_FILE_W, "w") as f:
    s = json.dumps(array_dict, indent=4)
    f.write(s)

#users_book = csv_dict//user_number


# with open(JSON_FILE_W, "w") as f:
#     s = json.dumps(result, indent=4)
#     print("выбранные данные 3", s)
#     print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
#     f.write(s)
