def get_num():
    while True:
        try:
            num = int(input("Введите целое число от 1 до 5: "))
            if 1 <= num <= 5:
                return num
            else:
                print("Ошибка: число должно быть в диапазоне от 1 до 5")
        except ValueError:
            print("Ошибка: нужно ввести целое число")

def translate_num(num):
    if num == 1:
        return "One"
    elif num == 2:
        return "Two"
    elif num == 3:
        return "Three"
    elif num == 4:
        return "Four"
    elif num == 5:
        return "Five"
    else:
        return "Unknown"


number = get_num()
translation = translate_num(number)
print(translation)


