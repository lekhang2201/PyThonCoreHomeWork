my_list = ["11", "22", "565", "OOP", "HTTPS"]
new_list = [i for i in my_list if len(str(i)) >= 2 and str(i)[-1] == str(i)[0]]
print(f"Số phần tử thỏa mãn là: {len(new_list)}")