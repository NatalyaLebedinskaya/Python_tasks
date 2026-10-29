def sum_list(list_1, list_2):
    result =[]
    min_length = len(list_1) if len(list_1) < len(list_2) else len(list_2)
    for i in range(min_length):
        result.append(list_1[i] + list_2[i])
    return result


numbers_1 = [1, 2, 3, 4, 5, 7]
numbers_2 = [11, 22, 33, 44, 55, 77]
print(f"Сумма элементов списков: {sum_list(numbers_1, numbers_2)}")
