def get_num():
    num = 0
    while num <= 0:
        try:
            num = int(input("Введите целое положительное число: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число")
    return num

def countdown(num):
    while num >= 0:
        print(num)
        num -= 1


number = get_num()
countdown(number)
