def mult(a, b):
    return a * b

print(mult(5, 10))


print((lambda x, y: x * y)(5, 10))


#my_list = [i for i in range(10)]
#even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
#sq_numbers = tuple(map(lambda x: x ** 2, my_list))
#print(even_numbers)
#print(sq_numbers)


products = {"apple": 10, "orange": 4, "banana": 15}

print(sorted(products.items(), key=lambda x: x[1]))
#products_items = [("apple", 10), ("orange", 4), ("banana", 15)]
print("products.items=", products.items())