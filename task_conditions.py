# Сумма всех четных чисел от 1 до 100
def sum_even_numbers():
    result = 0
    for num in range(1, 101):
        if num % 2 == 0:
            result += num
    return result


# Создание списка, содержащего квадраты всех нечетных чисел от 1 до 10
def squares_odd_numbers():
    data = [i ** 2 for i in range(1, 11) if i % 2 != 0]
    return data


# Запрос чисел, пока не введут отрицательное. Возвращает количество введеных чисел
def count_numbers():
    count = 0
    num = 0
    while num >= 0:
        try:
            num = int(input("Введите число: "))
            count += 1
        except ValueError:
            print("Ошибка: введено не число")
    return count


print(f"Сумма всех четных чисел от 1 до 100: {sum_even_numbers()}")
print(f"Квадраты всех нечетных чисел от 1 до 10: {squares_odd_numbers()}")
print(f"Количество введенных чисел: {count_numbers()}")
