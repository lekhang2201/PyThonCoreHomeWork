first_list = ["hhor", "1"]
second_list = [1, 2, 3, 5, 8, 7]
count = 0
for i in first_list:
    if i in second_list:
        count += 1
        break
print("2 list có phần tử chung") if count > 0 else print("2 list không có phần tử chung")