sample_dict = {
    'first_number': 1,
    'second_number': 2,
    'third_number': 3,
    'forth_number': 4,
    'duplicate_one': 1,
    'duplicate_four': 4,
    'duplicate_four_1': 5
}
list_value = list(sample_dict.values())
list_value.sort(reverse=True)
result = []
count = 0
for value in list_value:
    my_dict = {}
    for key in sample_dict.keys():
        if sample_dict.get(key) == value:
            count += 1
            my_dict.update({key: value})
            break
    result.append(my_dict)
    if count == 3:
        break
for i in result:
    print(i)