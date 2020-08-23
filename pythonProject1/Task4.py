my_list = [1, 2, 4, 5, (1, 5, 6), 9, 10]
count = 0
for i in my_list:
    if not isinstance(i, tuple):
        count += 1
    else:
        break
print(f"Result = {count}")