import pandas as pd
from files_hw import CSV_FILE
import json

# Step 1: Prepare the CSV File
#csv_file_path = 'path/to/csv/file.csv'

# Step 2: Read the CSV File
df = pd.read_csv(CSV_FILE)

# Step 3: Convert the CSV to JSON
json_string = df.to_json(orient='values')

# Step 4: Save the JSON File
json_file_path = 'output2.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json.dumps(json_string))
