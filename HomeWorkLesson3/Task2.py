string = input("Nhập vào một chuỗi: ")
m = int(input("Nhập vị trí muốn xóa: "))
if len(string) > 0 and 0 <= m < len(string) - 1:
    new_string = string[:m] + string[m+1:]
    print(f"Chuỗi mới: {new_string}")
else:
    print("Chuỗi hoặc vị trí bạn nhập không hợp lệ")
