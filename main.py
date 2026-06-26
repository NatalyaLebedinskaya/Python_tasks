# Простой калькулятор
try:
    print("Сложение")
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    print(f"{num_1} + {num_2} = {num_1 + num_2}\n")

    print("Вычитание")
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    print(f"{num_1} - {num_2} = {num_1 - num_2}\n")

    print("Умножение")
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    print(f"{num_1} * {num_2} = {num_1 * num_2}\n")

    print("Деление")
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    print(f"{num_1} / {num_2} = {num_1 / num_2}\n")

except ValueError:
    print("Ошибка: введено не числовое значение!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль! Второе число не должно быть равно 0")
finally:
    print("Программа завершена")
