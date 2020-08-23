my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
len_first_list = int(input("Nhập vào độ dài list đầu: "))
if len_first_list < len(my_list):
    new_first_list = my_list[:len_first_list]
    del my_list[:len_first_list]
    print(f"list 1 là: {new_first_list}, list 2 là: {my_list}")
else:
    print("Chỉ số bạn nhập không chính xác")
