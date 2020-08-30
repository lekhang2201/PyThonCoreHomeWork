my_string = input("Nhập vào một chuỗi: ")
temp_set = set(my_string)
temp_dict = {}.fromkeys(temp_set)
for i in temp_set:
    count = my_string.count(i)
    temp_dict.update({i: count})
print(f"Số lần ký tự xuất hiện trong chuỗi: {temp_dict}")