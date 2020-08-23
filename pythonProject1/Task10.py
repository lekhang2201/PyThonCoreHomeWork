my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
list_result = []
for i in my_list:
    temp_list = i.split(".")
    list_result.append(temp_list[-1])
print(list_result)