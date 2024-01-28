from files_hw import JSON_FILE

with open(JSON_FILE, "r") as file:
    print(file.read())
    # No need to call close method

print("\n", 20 * "=", "\n")

is_found = False
with open(JSON_FILE, "r") as file:
    for line in file.readlines():
        print(line)
        if 'Tyler Dotson' in line:
            is_found = True
            break

print("\n", 20 * "=", "\n")

file = open(JSON_FILE, 'r')
try:
    print(file.read())
# except Exception as e:
#     ...
finally:
    file.close()


class MyOpenFile:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with MyOpenFile(JSON_FILE, "r") as file:
    print(file.read())

my_context = MyOpenFile(JSON_FILE, "r")
try:
    file = my_context.__enter__()
    print(file.read())
finally:
    my_context.__exit__('exc_type', 'exc_val', 'exc_tb')
