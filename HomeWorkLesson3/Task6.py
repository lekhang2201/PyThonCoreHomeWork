my_string = input("Nhập vào 1 chuỗi: ")
new_string = ""
for char in my_string:
    if char.islower():
        new_string += char.upper()
    elif char.isupper():
        new_string += char.lower()
    else:
        new_string += char
print(f"Chuỗi mới là: {new_string}")