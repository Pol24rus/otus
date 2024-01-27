import json
import csv
from csv import DictReader

from files_hw import JSON_FILE, JSON_FILE_W2, CSV_FILE

result = []
with open(JSON_FILE, "r") as f:
    users = json.load(f)
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "Book": []})
        len(result)

with open(CSV_FILE, newline='') as f2:
    reader = DictReader(f2)
    array_dict = []
    # Итерируемся по данным делая из них словари
    for row in reader:
        array_dict.append(row)  # словарь книг
    print(array_dict)

user_count = len(result)  # кол-во пользователей
print("user_count", user_count)
book_count = len(array_dict)  # кол-во книг
print("book_count", book_count)
book_users = book_count // user_count  # кол-во книг на 1 пользователя
print("book_users", book_users)
remaining_books = book_count % user_count  # оставшиеся книги
print("remaining_book", remaining_books)
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])
print("index", 30 % user_count)

counter = 0
for users in result:
    print("=users=", users)
for book in array_dict:
    current_user_index = counter % user_count
    result[current_user_index]['Book'].append(book)
    print("all_book", result)
    # if counter >= 28:
    #     break
    # else:
    counter += 1

# for book in array_dict:
# current_user_index = тут нужно придумать формулу
# result[current_user_index]['Book'].append(book)

#         # print("result", result)
#         len(result)


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
