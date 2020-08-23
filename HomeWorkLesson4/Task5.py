import random

my_list = [1, 2, 3, 4, 1, 5, 3, 4, 8, 5, 5, 4, 1, 1, 5]
max_count = my_list.count(my_list[0])
new_list = list(set(my_list))
list_max_count = []
for i in new_list:
    if my_list.count(i) > max_count:
        count = my_list.count(i)
        list_max_count.clear()
        list_max_count.append(i)
    elif my_list.count(i) == max_count:
        list_max_count.append(i)
print(f"Phần tử xuất hiện nhiều nhất là {list_max_count[random.randint(0,len(list_max_count)-1)]}")