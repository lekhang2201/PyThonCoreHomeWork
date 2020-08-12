number_1 = int(input("Nhập số nguyên thứ 1: "))
number_2 = int(input("Nhập số nguyên thứ 2: "))
_max = max(number_1, number_2)
_min = min(number_1, number_2)
end_range = _max - (_max % 5)
start_range = _min - (_min % 5) + 5
count = 0
max_loop = abs(number_1 - number_2)/3
for i in range(start_range, end_range + 1, 5):
    count += 1
    print(i)
print("Số lần lặp: {s1}, số lần lặp tối đa {s2}".format(s1=count, s2=max_loop))
