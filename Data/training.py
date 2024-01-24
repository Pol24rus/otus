import json
import csv
from copy import deepcopy

from files_hw import JSON_FILE, JSON_FILE_W2, CSV_FILE

result = []

with open(JSON_FILE, "r") as f:
    users = json.load(f)
    user_number = 0
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "Book": []})
        user_number += 1

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


# result_2 = []
# for i in result:
# #    result_2 = deepcopy(result)
#     result_2.append["Book"] = array_dict
#     result_2 += 1
class Iteration:

    def __init__(self, result_2):
        self.result_2 = result_2


    def __iter__(self):
        self.result_1 = 0
        return self


    def __next__(self):
        if self.result_1 > len(self.result_2):
            raise StopIteration
        else:
            result_3 = self.result_1
            self.result_1 += 1
            return result_3

print('resultat')
for i in Iteration(array_dict):
    print(i)

# user_num = Iteration(result_3)
# my_iter = iter(user_num)

# with open(JSON_FILE_W, "w") as f:
#     s = json.dumps(result, indent=4)
#     print("выбранные данные 3", s)
#     print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
#     f.write(s)
