import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV_FILE = get_path('books.csv')
JSON_FILE = get_path('users.json')
# YAML_FILE = get_path('config.yaml')

CSV_FILE_W = get_path('books_w.json')
JSON_FILE_W = get_path('result.json')
JSON_FILE_W2 = get_path('training_w.json')
CSV_TO_JSON_FILE_W = get_path('book_json.json')
