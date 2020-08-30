my_dict = {
    'first_number': 1,
    'second_number': 2,
    'third_number': 3,
    'forth_number': 4,
    'duplicate_one': 1
}
list_key = list(my_dict.keys())
list_key.sort(reverse=True)
for i in list_key[:3]:
    print(my_dict.get(i))