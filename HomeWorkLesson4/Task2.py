my_list = [1, 2, 3, 4, 5, 6, 7, 88, 100]
sum_element = 0
multiple_element = 1
for i in my_list:
    sum_element += i
    multiple_element *= i
print(f"Tổng các phần tử trong list là {sum_element}, Tích các phần tử trong list là: {multiple_element}")