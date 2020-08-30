sample_dict = {
    'first_number': 1,
    'second_number': 2,
    'third_number': 3,
    'forth_number': 4,
    'duplicate_one': 1
}
my_dict = {}
my_list_key = ['first_number', 'second_number', 0, 3, 'duplicate_one']
for key in my_list_key:
    if key in sample_dict.keys():
        my_dict.update({key: sample_dict[key]})
print(my_dict)
