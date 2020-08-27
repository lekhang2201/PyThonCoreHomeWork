# 1.1 Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím.
from constants import constant

my_string = input("Nhập vào một chuỗi: ")
max_char = max(my_string)
min_char = min(my_string)
print(f"Ký tự lớn nhất là: {max_char}, Ký tự nhỏ nhất là: {min_char}")
print("Done 1.1")

# 1.2 Viết chương trình nhập vào một số nguyên dương, tính tổng các chữ số của nó.
number_input = input("Nhập vào một số nguyên dương: ")
if number_input.isnumeric() and int(number_input) > constant.INT_ZERO:
    result = 0
    for i in number_input:
        result += int(i)
    print(f"Tổng các chữ số trong số đã cho là: {result}")
else:
    print("Chuỗi bạn vừa nhập không phải 1 số nguyên dương")

# 1.3 Viết hàm đếm số lần xuất hiện các ký tự trong một String.
my_string = input("Nhập vào một chuỗi: ")
temp_set = set(my_string)
temp_dict = {}.fromkeys(temp_set)
for i in temp_set:
    count = my_string.count(i)
    temp_dict.update({i: count})
print(f"Số lần ký tự xuất hiện trong chuỗi: {temp_dict}")
