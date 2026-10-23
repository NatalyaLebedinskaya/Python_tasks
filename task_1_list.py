def swap_first_last(input_list):
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list


numbers = [11, 22, 33, 44, 55]
print(f"Исходный список: {numbers}")
print(f"Измененный список: {swap_first_last(numbers)}")