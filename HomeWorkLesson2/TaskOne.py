import math

a = float(input("Nhập hệ số a = "))
b = float(input("Nhập hệ số b = "))
c = float(input("Nhập hệ số c = "))
result = ""
if a == 0:
    if b == 0 and c != 0:
        result = "Phương trình vô nghiệm"
    elif b == 0 and c == 0:
        result = "Phương trình có vô số nghiệm"
    else:
        result = "Phương trình có nghiệm duy nhất: x = {x}".format(x=-c / b)
else:
    const = -b / (2 * a)
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        result = "Phương trình có nghiệm kép: x1 = x2 = {x}".format(x=const)
    elif delta < 0:
        result = "Phương trình có hai nghiệm phức x1 = {x1}, x2 = {x2}".format(
            x1=complex(const, math.sqrt(-delta) / (2 * a)),
            x2=complex(const, -math.sqrt(-delta) / (2 * a))
        )
    else:
        result = "Phương trình có hai nghiệm thực phân biệt: x1 = {x1}, x2 = {x2}".format(
            x1=(const + math.sqrt(delta) / (2 * a)),
            x2=(const - math.sqrt(delta) / (2 * a))
        )
print(result)