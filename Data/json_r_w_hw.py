import json
from files_hw import JSON_FILE, JSON_FILE_W

result = []
with open(JSON_FILE, "r") as f:
    users = json.load(f)
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'],
                       "address": i['address'], "age": i['age'], "Book": ['2']})
        len(result)

with open(JSON_FILE_W, "w") as f:
    s = json.dumps(result, indent=4)
    print("выбранные данные 3", result)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    f.write(s)
