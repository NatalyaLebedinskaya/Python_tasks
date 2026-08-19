#принимает два числа и возвращает наибольшее из них
def max_number(a, b):
    try:
        return sorted([a, b])[1]
    except (TypeError, ValueError):
        print("Аргументы должны быть числами")


#ничего не делает
def empty_function():
    pass


#генерирует все четные числа от 0 до n включительно
def even_numbers(n):
    try:
        n = int(n)
        for num in range(0, n + 1, 2):
            yield num
    except (TypeError, ValueError):
        print("Аргумент должен быть числом")


#автотест для функции max_number(a, b)
def test_max_number():
    assert max_number(5, 1) == 5, "Ошибка: функция max_number(5, 1) должна вернуть 5"
    assert max_number(3, 7) == 7, "Ошибка: функция max_number(3, 7) должна вернуть 7"
    assert max_number(-5, -25) == -5, "Ошибка: функция max_number(-5, -25) должна вернуть -5"
    assert max_number(11, 11) == 11, "Ошибка: функция max_number(11, 11) должна вернуть 11"
    assert max_number(0, 0) == 0, "Ошибка: функция max_number(0, 0) должна вернуть 0"
    assert max_number("fewf", 1) == None, "Ошибка: функция max_number('fewf', 1) должна вернуть None"
    print("Все тесты пройдены!")


print(list(even_numbers("hh")))
test_max_number()