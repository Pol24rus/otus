import json
from files_hw import JSON_FILE, JSON_FILE_W

result = []

with open(JSON_FILE, "r") as f:
    users = json.load(f)
    #    print(users[1])  # возвращает полностью данные по человеку
    # выбираю нужные данные из индекса
    user_number = 0
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'], "age": i['age']})
        user_number += 1


with open(JSON_FILE_W, "w") as f:
    s = json.dumps(result, indent=4)
    print("выбранные данные 3", s)
    f.write(s)
