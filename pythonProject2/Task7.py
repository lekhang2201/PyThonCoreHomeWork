

first_dict = {
    'first_number': 1,
    'second_number': 2,
    'third_number': 3,
    'forth_number': 4,
    'duplicate_one': 1
}
second_dict = {
    'first_number': 1,
    'second_number': 3,
    'third_number': 5,
    'forth_number': 4,
    'duplicate_one': 1,
    'zero': 0
}
my_dict = {}.fromkeys()
for item in first_dict.items():
    if item in second_dict.items():
        my_dict.update({item[0]: item[1]})
print(my_dict)