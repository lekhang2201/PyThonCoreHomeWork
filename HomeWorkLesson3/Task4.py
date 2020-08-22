string = input("Nhập vào một chuỗi: ")
if len(string) < 2:
    print("Chuỗi mới là: ")
else:
    new_string = string[0:2] + string[-2:]
    print(f"Chuỗi mới là: {new_string}")
