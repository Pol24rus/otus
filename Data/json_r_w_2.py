import json
from files_hw import JSON_FILE, JSON_FILE_W

with open(JSON_FILE, "r") as f:
    # users = json.loads(f.read())
    users = json.load(f)
    #    print(users[1])  # возвращает полностью данные по человеку
    # выбираю нужные данные из индекса
    for i in users:
        data_user = i['name'], i['gender'], i['address'], i["age"]
#        print("выбранные данные", data_user)
        data = {
            "data_user": [
                {"name": i['name'], "gender": i['gender'], "address": i['address'], "age": i['age']}
            ]
        }
        # data_user_2 = (json.dumps(data_user, indent=4))
        # print("выбранные данные 2 ", data_user_2)
#        print('/' * 20)
        print("сортированные данные", data)
        print('*************************************************')


with open(JSON_FILE_W, "w") as f:
    s = json.dumps(data, indent=4)
    print("выбранные данные 3", s)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    f.write(s)
