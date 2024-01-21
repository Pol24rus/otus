import json
from files_hw import JSON_FILE, JSON_FILE_W

with open(JSON_FILE, "r") as f:
    # users = json.loads(f.read())
    users = json.load(f)
    #    print(users[1])  # возвращает полностью данные по человеку
    # выбираю нужные данные из индекса
    for i in users:
        data_user = i['name'], i['gender'], i['address'], i["age"]
        print("выбранные данные", data_user)
        data_user_2 = (json.dumps(data_user, indent=4))
        print("выбранные данные 2 ", data_user_2)
        print('/' * 20)


with open(JSON_FILE_W, "w") as f:
    #    s = json.dumps(data_user, indent=4)
    print("выбранные данные 3", data_user_2)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    f.write(data_user_2)
