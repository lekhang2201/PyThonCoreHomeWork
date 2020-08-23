first_tuple = (1, 2, 3, 4)
second_tuple = (0, 5, 6)
result = "No"
for i in first_tuple:
    if i in second_tuple:
        result = "Yes"
        break
print(result)
