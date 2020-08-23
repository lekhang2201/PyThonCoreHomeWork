import random

my_list = [1, 21, 3, 5, "ABC", "abc", 10, 11, 15, "đây là một phần tử trong list"]
new_list = []
for i in range(5):
    random_index = random.randint(0, len(my_list) - 1)
    new_list.append(my_list[random_index])
print(f"List mới là: {new_list}")
