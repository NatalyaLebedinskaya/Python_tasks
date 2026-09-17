def check_password(right_password):
    user_password = ""
    while user_password != right_password:
        user_password = input("Введите пароль: ")
    print("Пароль верный")


check_password("Natasha")