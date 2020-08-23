my_list = [(2, 6, 8), (4, 1), (0, 0, 8)]
min_tuple = my_list[0]
for i in my_list:
    if len(i) >= 2 and len(min_tuple) >= 2:
        if i[1] < min_tuple[1]:
            min_tuple = i
print(min_tuple)