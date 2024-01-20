import json
from files_hw import JSON_FILE, JSON_FILE_W

with open(JSON_FILE, "r") as f:
    # users = json.loads(f.read())
    users = json.load(f)
    for i in users['name']['address']:
        print(i)
# users_list = (users['name'], users['address'])
# print(users_list)
# for user in users:
#    print(user["name"], user["address"])

# #print(100 * "+")  # Write
# user = {
#     "users": [
#         {"name": (users["name"]), "address": (users["address"])}
# #         # {"login": "Plaksa", "email": "cat@gmail.ru"},
# # #         # {"login": "MMayers", "email": "fromhellwithlove@gmail.com"},
#     ]
#  }
# print(user)
# with open(JSON_FILE_W, "w") as f:
#     s = json.dumps(user, indent=4)
#     f.write(s)
