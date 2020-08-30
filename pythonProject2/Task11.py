my_string = input("Nhập vào một câu: ")
temp_set = set(my_string.split())
temp_dict = {}.fromkeys(temp_set)
for i in temp_set:
    count = my_string.count(i)
    temp_dict.update({i: count})
print(f"Số lần xuất hiện các từ trong chuỗi: {temp_dict}")