new_list = []

for num in range(1, 13):
    if num % 2 == 0:
        new_list.append(num)

print(new_list)

integer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#new_list_2 = [num if num % 2 == 0 else num + 1 for num in range(11) ]
#print(list(new_list_2))


new_gen = (num for num in integer if num % 2 == 0)
print("new_gen= ", new_gen)

#keys = ["a", "b", "c"]
#values = [1, 2, 3]

#key_value = {k: v for k, v in zip(keys, values) if v %2 ==1}
#print(key_value)
