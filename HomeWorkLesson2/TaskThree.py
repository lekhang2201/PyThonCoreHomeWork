n = input("Nhập số n < 1000: ")
res = ""
if float(n) >= 1000:
    res = "Số bạn nhập không nhỏ hơn 1000"
else:
    total = 0
    for i in n:
        if i.isdigit():
            total += int(i)
    res = "Tổng các chữ số trong n là: {x}".format(x=total)
print(res)
