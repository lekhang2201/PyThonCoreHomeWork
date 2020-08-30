my_list = [{'item': 'item1', 'amount': 400},
           {'item': 'item2', 'amount': 300},
           {'item': 'item1', 'amount': 750},
           {'item': 'item3', 'amount': 750},
           {'item': 'item1', 'amount': 100},
           {'item': 'item2', 'amount': 750}]
list_item = []
my_dict = {}.fromkeys(list_item)
for index in range(len(my_list)):
    if my_list[index].get('item') not in list_item:
        list_item.append(my_list[index].get('item'))
for item in list_item:
    value = 0
    for element in my_list:
        if element.get('item') == item:
            value += element.get('amount')
    my_dict.update({item: value})
print(my_dict)