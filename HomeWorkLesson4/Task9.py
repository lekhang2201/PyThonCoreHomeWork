first_matrix = [[1, 2, 3], [1, 1, 1], [-1, 2, 5]]
second_matrix = [[2, 2, 5], [0, 1, 1], [-1, -3, 5]]
result = []
for i in range(3):
    element_result = []
    element = 0
    for j in range(3):
        element += first_matrix[i][j] * second_matrix[j][i]
        element_result.append(element)
    result.append(element_result)
print(result)
