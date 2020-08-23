my_list = [1, 2, 4, 6, 7, 84, 2, 3, 52, 32, 23, 2, 1]
count = 0
for i in range(len(my_list)):
    for j in range(i, len(my_list)):
        if my_list[i] > my_list [j]:
            count += 1
print(f"Số cặp dược tạo là: {count}")
