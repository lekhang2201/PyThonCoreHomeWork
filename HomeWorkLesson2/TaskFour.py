a = float(input("Nhập độ dài cạnh a = "))
b = float(input("Nhập độ dài cạnh b = "))
c = float(input("Nhập độ dài cạnh c = "))
half_cir = (a + b + c) / 2
res = ""
if half_cir - a <= 0 or half_cir - b <= 0 or half_cir - c <= 0:
    res = "Ba số đã cho không phải là 3 cạnh của 1 tam giác"
else:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        res = "Ba số đã cho là ba cạnh của 1 tam giác vuông"
    else:
        res = "Ba số đã cho là ba cạnh của 1 tam giác không vuông"
print(res)