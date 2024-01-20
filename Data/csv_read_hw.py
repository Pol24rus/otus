import csv
from csv import DictReader
from files_hw import CSV_FILE

with open(CSV_FILE, newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)[:4]
    header[2],header[3] = header[3],header[2]
    # print(header[0])
    # print(header[1])
    # print(header[2])
    # print(header[3])

    # Итерируемся по данным делая из них словари
    for row in reader:
        row[2],row[3] = row[3],row[2]
#        print(row)
        csv_dict = dict(zip(header, row)) # делает словарь с ключом
        print(csv_dict)
#        print(dict(zip(header, row)))
#        print('********************************')
