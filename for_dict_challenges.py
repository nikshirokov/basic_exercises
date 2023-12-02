# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = dict()

for student in students:
    if student['first_name'] not in names:
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

for name, count in names.items():
    print(f'{name}: {count}')
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = dict()

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

max_count=max(names.values())
for name, count in names.items():
    if count == max_count:
        print(name)
print()

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
names = dict()

for students in school_students:
    for student in students:
        if student['first_name'] not in names.keys():
            names[student['first_name']] = 1
        else:
            names[student['first_name']] += 1
        max_count = max(names.values())
    for name, count in names.items():
        if count == max_count:
            print(f'Самое частое имя в классе {school_students.index(students)+1}: {name}')
    names.clear()
print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    boys_count = 0
    girl_count = 0
    for students in school_class['students']:
        for name in students.values():
            if is_male[name]:
                boys_count += 1
            else:
                girl_count += 1
    print(f'Класс {school_class["class"]}: девочки {girl_count}, мальчики {boys_count}')
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
class_school={}
for school_class in school:
    class_school[school_class["class"]] = {"boys_count": 0, "girls_count": 0}
    for students in school_class['students']:
        for name in students.values():
            if is_male[name]:
                class_school[school_class["class"]]["boys_count"] += 1
            else:
                class_school[school_class["class"]]["girls_count"] += 1
clas_with_max_girl = ''
max_boys = 0
max_girls = 0
clas_with_max_boy = ''
for clas in class_school.keys():
    if max_boys < class_school[clas]['boys_count']:
        max_boys = class_school[clas]['boys_count']
        clas_with_max_boy = clas
    if max_girls < class_school[clas]['girls_count']:
        max_girls = class_school[clas]['girls_count']
        clas_with_max_girl = clas
print(f'Больше всего мальчиков в классе {clas_with_max_boy}')
print(f'Больше всего девочек в классе {clas_with_max_girl}')
