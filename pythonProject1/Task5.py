my_list = [(2, 5, 6), (4, 1), (0, 0, 8)]
for i in range(len(my_list)):
    for j in range(i, len(my_list)):
        if my_list[i][-1] > my_list[j][-1]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)