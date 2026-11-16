# Вычисляет средний балл студента
def calculate_average(grades):
    return sum(grades) / len(grades)


# Вычисляет общий средний балл всех студентов
def calculate_overall_average(student_list):
    if not student_list:
        return 0
    grades_sum = 0
    for student in student_list:
        grades_sum += calculate_average(student["grades"])
    overall_average_grade = grades_sum / len(student_list)
    return overall_average_grade


# Вычисляет студента с самым низким баллом
def calculate_lowest_grade_student(student_list):
    lowest_grade_student = student_list[0]
    lowest_average_grade = calculate_average(lowest_grade_student["grades"])
    for student in student_list:
        average = calculate_average(student["grades"])
        if average < lowest_average_grade:
            lowest_average_grade = average
            lowest_grade_student = student
    print(f"Cтудент с самым низким баллом: {lowest_grade_student['name']} \n")
    return lowest_grade_student


# Выводит информацию по всем студентам
def print_students_info(student_list):
    for student in student_list:
        # Вычисляем средний балл студента
        average = calculate_average(student["grades"])
        # Определяем студент успешен или отстающий
        status = "Успешен" if average >= 75 else "Отстающий"
        # Выводим информацию по студенту
        print(f"Студент: {student['name']}")
        print(f"Средний балл: {average:.2f}")
        print(f"Статус: {status} \n")
    print(f"Общий средний балл: {calculate_overall_average(student_list):.2f} \n")


# Создаем список студентов
students = [
    {"name": "Иванов", "grades": [87, 99, 85], },
    {"name": "Петрова", "grades": [80, 90, 77], },
    {"name": "Смирнов", "grades": [95, 97, 90],},
    {"name": "Кузнецова", "grades": [60, 72, 75],},
]

# Выводим информацию по всем студентам
print_students_info(students)

# Добавляем нового студента
new_student = {"name": "Соколов", "grades": [85, 88, 92]}
students.append(new_student)
calculate_overall_average(students)

# Удаляем студента с самым низким баллом
students.remove(calculate_lowest_grade_student(students))
calculate_overall_average(students)

# Выводим обновленную информацию по всем студентам
print_students_info(students)
