number_1 = int(input("Nhập số nguyên thứ 1: "))
number_2 = int(input("Nhập số nguyên thứ 2: "))
_max = max(number_1, number_2)
_min = min(number_1, number_2)
end_range = _max - (_max % 5)
start_range = _min - (_min % 5) + 5
for i in range(start_range, end_range + 1, 5):
    print(i)
