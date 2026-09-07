def get_num():
    num = 0
    while num < 1 or num > 5:
        try:
            num = int(input("Введите целое число от 1 до 5: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число")
    return num

def translate_num(num):
    translator = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
    if num in translator:
        return translator[num]
    else:
        return "Unknown"


number = get_num()
translation = translate_num(number)
print(translation)
