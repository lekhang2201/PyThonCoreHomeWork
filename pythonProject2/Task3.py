my_dict = {
    'first_number': 1,
    'second_number': 2,
    'third_number': 3,
    'forth_number': 4
}
list_key = list(my_dict.keys())
list_key.sort(reverse=False)
new_dict = {}
for key in list_key:
    new_dict.update({key: my_dict.get(key)})
print(new_dict)
