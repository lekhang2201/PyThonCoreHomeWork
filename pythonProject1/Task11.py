my_string = input("Nhập vào 1 câu: ")
temp_list = my_string.split()
temp_list.sort(key=len, reverse=True)
print(temp_list[0])