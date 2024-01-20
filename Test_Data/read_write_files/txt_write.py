from files import TXT_FILE_W

some_file = open(TXT_FILE_W, "w")  # w, a

text = """когда илье звонит начальник
он сразу трубку не берет
а выжидает полминуты
и в это время он бунтарь
"""

# some_file.write(text)

# write list
some_file.writelines(['строка1\n', 'строка2\n', 'строка3\n']) # \n

some_file.close()
