my_dict = {
    'first_number': 1,
    'second_number': 2,
    'this_is_string': 'my_string',
    'android': 'Kotlin',
    'machine_learning': 'Python'
}
result = 1
for i in my_dict.values():
    if isinstance(i, int) or isinstance(i, float):
        result *= i
print(f"Tich cac value la: {result}")
