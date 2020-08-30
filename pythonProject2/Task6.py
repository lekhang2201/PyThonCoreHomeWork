number_element_of_dict = int(input("Nhập số phần tử của Dictionary (lớn hơn 3): "))
number_element_of_list = int(input("Nhập số phần tử của Value List (lớn hơn 5): "))
my_dict = {}
if number_element_of_dict <= 3 or number_element_of_list <= 5:
    print("Giá trị nhập không đúng")
else:
    for i in range(1, number_element_of_dict + 1):
        element_of_dict = []
        print(f"Nhập phần tử cho list {i}")
        for j in range(1, number_element_of_list + 1):
            element_of_list = input(f"Nhập phần tử thứ {j} trong list: ")
            element_of_dict.append(element_of_list)
        my_dict.update({i: element_of_dict})
    for key in my_dict.keys():
        print(my_dict.get(key)[4])