A = [1, 1, 2, 5, 3, 2, 1, 5, 3, 6, 7, 8, 6, 9]
result = []
for i in A:
    if i not in result:
        result.append(i)
print(f"vì chuỗi hình thành được là: {result}")