x = float(input("Nhập số thực x = "))
n = int(input("Nhập số nguyên dương n = "))
s1 = 0
s2 = 0
s3 = 0
if n <= 0:
    print("Số n bạn nhập không phải số nguyên dương")
else:
    for i in range(n + 1):
        giai_thua_i = 1
        s1 += x ** i
        s2 += ((-1) ** i) * (x ** i)
        for j in range(i + 1):
            if j == 0:
                giai_thua_i = 1
            else:
                giai_thua_i *= j
        s3 += x ** i / giai_thua_i
print("Kết quả: s1 = {s1}, s2 = {s2}, s3 = {s3}".format(s1=s1, s2=s2, s3=s3))
