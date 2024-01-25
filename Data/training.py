import json
import csv

from files_hw import JSON_FILE, JSON_FILE_W2, CSV_FILE

result = []
with open(JSON_FILE, "r") as f:
    users = json.load(f)
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "Book": []})
        len(result)

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

user_count = len(result)  # кол-во пользователей
print("user_count", user_count)
book = len(array_dict)  # кол-во книг
print("book_count", book)
book_users = book // user_count  # кол-во книг на 1 пользователя
print("book_users", book_users)
print("result", result[0])
print(result[1])

all_book = []
result = [0]
counter = 0
for users in result:
    for book in array_dict[:4]:

        current_user_index = result
        print("current_user_index", current_user_index)
        current_user_index += 1
        # result[current_user_index]['Book'].append(book)
        print("result", result)


with open(JSON_FILE_W2, "w") as f:
    s = json.dumps(result, indent=4)
    # print("выбранные данные 3", s)
    # print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    f.write(s)

# iteration
# class Iteration(itog):
#     itog = Iteration(csv_dict)
#     itr = itog.iterator()
#
#     while True:
#         try:
#             itr.next()
#         except StopIteration:
#             break
#         print(itr.current())
#
#     itr.first()
#
#     while True:
#         try:
#             itr.next()
#         except StopIteration:
#             break
#         print(itr.current())

# iteration
#     def __init__(self, result_2):
#         self.result_2 = result_2
#
#
#     def __iter__(self):
#         self.result_1 = 0
#         return self
#
#
#     def __next__(self):
#         if self.result_1 > self.result_2:
#             raise StopIteration
#         else:
#             result_3 = self.result_1
#             self.result_1 += 1
#             return result_3
#
# print('resultat')
# for i in range(self(result)):
#     print(i)

# user_num = Iteration(result_3)
# my_iter = iter(user_num)
# # объединил два списка
# combined_list = [i for i["Book"] in result + array_dict]
# print(combined_list)

# # объединил два списка
# result.append([array_dict])

# deepcopy
# result_2 = []
# for i in result:
# #    result_2 = deepcopy(result)
#     result_2.append["Book"] = array_dict
#     result_2 += 1
