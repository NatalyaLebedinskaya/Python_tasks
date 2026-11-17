# Вычисляет средний балл студента
def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)


# Вычисляет общий средний балл всех студентов, не учитывая студентов без оценок
def calculate_overall_average(student_list):
    grades_sum = 0
    count_students = 0
    for student in student_list:
        average = calculate_average(student["grades"])
        if average is not None:
            grades_sum += average
            count_students += 1
    overall_average_grade = (grades_sum / count_students if count_students > 0 else 0)
    return overall_average_grade


# Вычисляет студента с самым низким баллом, не учитывая студентов без оценок
def calculate_lowest_grade_student(student_list):
    lowest_grade_student = ""
    lowest_average_grade = 101
    for student in student_list:
        average = calculate_average(student["grades"])
        if average is not None and average < lowest_average_grade:
            lowest_average_grade = average
            lowest_grade_student = student
    return lowest_grade_student


# Выводит информацию по всем студентам
def print_students_info(student_list):
    for student in student_list:
        # Вычисляем средний балл студента
        average = calculate_average(student["grades"])
        if average is not None:
            # Определяем студент успешен или отстающий
            status = "Успешен" if average >= 75 else "Отстающий"
            # Выводим информацию по студенту
            print(f"Студент: {student['name']}\n"
                  f"Средний балл: {average:.2f}\n"
                  f"Статус: {status}\n")
        else:
            print(f"Студент: {student['name']}\n"
                  f"Средний балл: нет оценок\n"
                  f"Статус: нет данных\n")
    print(f"Общий средний балл: {calculate_overall_average(student_list):.2f} \n")


# Добавляет нового студента
def add_student(student_list, name, grades):
    # Проверяем, что имя в виде строки
    if type(name) != str:
        print("Ошибка: имя должно быть строкой.")
        return

    # Проверяем тип данных оценок, делаем их списком при необходимости
    if type(grades) == str:
        try:
            # Заменяем запятые на пробелы (например был ввод "85, 88, 92" или "85, 88, 92" или "85 88 92")
            clean_grades = grades.replace(",", " ")
            # Разбиваем по пробелам и превращаем в числа
            grades = [int(g) for g in clean_grades.split()]
        except ValueError:
            print("Ошибка: в строке оценок должны быть только числа через пробел или запятые")
            return
    # Проверяем, что оценки - это список
    elif type(grades) != list:
        print("Ошибка: оценки должны быть списком")
        return

    new_student = {"name": name, "grades": grades}
    student_list.append(new_student)
    calculate_overall_average(student_list)

# Удаляет студента
def remove_student(student_list, student):
    if student:
        student_list.remove(student)
        calculate_overall_average(student_list)


# Создаем список студентов
students = [
    {"name": "Семенов", "grades": [] },
    {"name": "Иванов", "grades": [87, 99, 85]},
    {"name": "Петрова", "grades": [80, 90, 77]},
    {"name": "Смирнов", "grades": [95, 97, 90]},
    {"name": "Кузнецова", "grades": [60, 72, 75]},
]

# Выводим информацию по всем студентам
print_students_info(students)

# Добавляем новых студентов
add_student(students,"Соколов","85, 88 92")

name_input = input("Введите имя нового студента: ")
grades_input = input("Введите оценки через пробел или запятые: ")
add_student(students, name_input, grades_input)

# Удаляем студента с самым низким баллом
lowest_student = calculate_lowest_grade_student(students)
remove_student(students, lowest_student)

# Выводим обновленную информацию по всем студентам
print_students_info(students)
