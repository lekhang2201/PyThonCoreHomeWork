first_string = input("Nhập vào một chuỗi: ")
if len(first_string) > 0:
    first_string = first_string.replace(first_string[0], "$")
print(first_string)
