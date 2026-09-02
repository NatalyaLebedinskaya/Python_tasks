def get_age():
    while True:
      try:
        age = int(input("Введите ваш возраст: "))
        return age
      except ValueError:
        print("Ошибка:нужно ввести число")


def get_citizenship():
    while True:
      answer = input("Вы являетесь гражданином страны? (да/нет)").strip().lower()
      if answer == "да":
        return True
      elif answer == "нет":
        return False
      else:
        print('Ошибка: введите "да" или "нет"')


def get_disqualification():
    while True:
      answer = input("Есть ли у вас судимость или вы дисквалифицированы по другой причине? (да/нет)").strip().lower()
      if answer == "да":
        return True
      elif answer == "нет":
        return False
      else:
        print('Ошибка: введите "да" или "нет"')


def can_vote(age, is_citizen, is_disqualified):
    return age >= 18 and is_citizen and not is_disqualified


def print_result(can_vote_result):
    if can_vote_result:
        print("Вы можете голосовать на выборах")
    else:
        print("Вы не имеете право голосовать на выборах")

age = get_age()
is_citizen = get_citizenship()
is_disqualified = get_disqualification()
can_vote_result = can_vote(age, is_citizen, is_disqualified)
print_result(can_vote_result)