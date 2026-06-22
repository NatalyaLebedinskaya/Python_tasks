print(f"Деление двух чисел")
try:
    num_1 = float(input("Введите первое число:"))
    num_2 = float(input("Введите второе число:"))
    result = num_1 / num_2
    print(f"{num_1} / {num_2} = {result}")
except ValueError:
    print("Ошибка: введено не числовое значение!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль! Второе число не должно быть равно 0")
finally:
    print("Программа завершена")