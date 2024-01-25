users = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 40},
    {"Book": []}
]

books = [
    {"book": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 40}
]

bookCount = 10
userCount = len(users)
resCount = bookCount // userCount  # Number of books per user
count = 0
counter = 0

for user in users:
    count += 1
    if count == userCount - 1:
        resCount = bookCount - counter
    for i in range(counter, counter + resCount):
        users["Book"] = books[i]
    counter += resCount
