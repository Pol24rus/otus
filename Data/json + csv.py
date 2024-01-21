import json
import csv
from files_hw import JSON_FILE, JSON_FILE_W
from files_hw import CSV_FILE

with open(JSON_FILE, "r") as f:
    # users = json.loads(f.read())
    users = json.load(f)
    #    print(users[1])  # возвращает полностью данные по человеку
    # выбираю нужные данные из индекса
    for i in users:
        data_user = i['name'], i['gender'], i['address'], i["age"]
#        print("выбранные данные", data_user)
        data_user_2 = (json.dumps(data_user, indent=4))
        print("выбранные данные - 2 ", data_user_2)
        print('/' * 20)

with open(CSV_FILE, newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)[:4]
    header[2],header[3] = header[3],header[2]

    # Итерируемся по данным делая из них словари
    for row in reader:
        row[2],row[3] = row[3],row[2]
        csv_dict = dict(zip(header, row)) # делает словарь с ключом
        print('csv_dict ',csv_dict)
#        print(dict(zip(header, row)))
