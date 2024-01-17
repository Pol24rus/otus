import itertools
import functools
from time import sleep
from datetime import datetime

example = [[1, 2, 3, 4, 5], ["some", "something"]]

#print(list(itertools.chain(*example)))

#print(list(itertools.repeat('sex', 5)))

#print(list(itertools.combinations([1, 2, 3, 4], 2)))
print(list(itertools.permutations([1, 2, 3, 4], 2)))


# functools.lru_cache
@functools.lru_cache()
def slow_func(a, b, ):
    sleep(1)
    return a * b


print("Start")
start = datetime.now()

for i in range(5):
    slow_func(1, 5)

print(f"End: {datetime.now() - start}")

