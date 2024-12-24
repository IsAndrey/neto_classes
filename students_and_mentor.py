MIN_GRADE = 0
MAX_GRADE = 10

DATA = {
    'Students': [
        [1, 'Геннадий', 'Сидоров', 'муж'],
        [2, 'Аркадий', 'Райкин', 'муж'],
        [3, 'Фаина', 'Раневская', 'жен'],
        [4, 'Джодж', 'Буш', 'муж'],
        [5, 'Кандолиза', 'Райз', 'жен'],
        [6, 'Филип', 'Киркоров', 'муж'],
        [7, 'Татьяна', 'Буланова', 'жен'],
        [8, 'Илон', 'Маск', 'муж'],
        [9, 'Александр', 'Суворов', 'муж'],
        [10, 'Екатерина', 'Великая', 'жен'], 
    ],
    'Lectureres': [
        [1, 'Сахиб', 'Болтонбаев'],
        [2, 'Мустафа', 'Хамраев'],
        [3, 'Тулкин', 'Ядыгханов'],
        [4, 'Равшан', 'Холмухаммедов']
    ],
    'Reviwers': [
        [1, 'Сахиб', 'Болтонбаев'],
        [2, 'Мустафа', 'Хамраев'],
        [3, 'Тулкин', 'Ядыгханов'],
        [4, 'Равшан', 'Холмухаммедов']
    ],
    'Courses': [
        [1, 'Питон для чайников.'],
        [2, '1C не для чайников.']
    ],
    'Finished_courses': [
        [1, 1], [2, 1], [3, 1], [4, 1], [5, 1],
        [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]
    ],
    'Courses_in_progress': [
        [1, 2], [2, 2], [3, 2], [4, 2], [5, 2],
        [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]
    ],
    'Attached_courses_reviewers': [
        [1, 1], [2, 1], [3, 2], [4, 2]
    ],
    'Attached_courses_lectures': [
        [1, 1], [2, 1], [3, 2], [4, 2]
    ],
    'Lectureres_grades': [
        [1, 1, 1, 3], [1, 2, 1, 10],
        [2, 1, 1, 7], [2, 2, 1, 4],
        [3, 1, 1, 10], [3, 2, 1, 5],
        [4, 1, 1, 5], [4, 2, 1, 8],
        [5, 1, 1, 2], [5, 2, 1, 9],
        [6, 3, 2, 9], [6, 4, 2, 1],
        [7, 3, 2, 4], [7, 4, 2, 10],
        [8, 3, 2, 0], [8, 4, 2, 6],
        [9, 3, 2, 8], [9, 4, 2, 7],
        [10, 3, 2, 3], [10, 4, 2, 2]
    ],
    'Students_grades': [
        [1, 3, 2, 8], [1, 4, 2, 5],
        [2, 3, 2, 9], [1, 4, 2, 6],
        [3, 3, 2, 7], [1, 4, 2, 2],
        [4, 3, 2, 5], [1, 4, 2, 10],
        [5, 3, 2, 8], [1, 4, 2, 9],
        [6, 1, 1, 9], [6, 2, 1, 6],
        [7, 1, 1, 10], [7, 2, 1, 8],
        [8, 1, 1, 2], [8, 2, 1, 3],
        [9, 1, 1, 10], [9, 2, 1, 4],
        [10, 1, 1, 4], [10, 2, 1, 10]
    ]
}

STUDENTS = []
LECTURERES = []
REVIEWERS = []

class Person:
    def __init__(self, name, surname, gender=None):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def __eq__(self, value):
        if isinstance(value, Person):
            return self.average_grade() == value.average_grade()

    def __lt__(self, value):
        if isinstance(value, Person):
            return self.average_grade() < value.average_grade()

    def __le__(self, value):
        if isinstance(value, Person):
            return self.average_grade() <= value.average_grade()

    def set_grade(self, course, grade, control_list=None):
        if control_list is not None and course not in control_list:
            return f'Ошибка: курс {course} не в списке {control_list}'
        if grade not in range(MIN_GRADE, MAX_GRADE):
            return f'Ошибка: оценка {grade} не входит в диапазон {MIN_GRADE}:{MAX_GRADE} у {self} за курс {course}'
        if course in self.grades:
            self.grades[course] += [grade]
        else:
            self.grades[course] = [grade]

    def give_grade(self, person, course, grade, control_type=None, control_list=None):
        if not isinstance(person, control_type):
            return f'Ошибка: объект {person} не является экземпляром класса {control_type}'
        if control_list is not None and not course in control_list:
            return f'Ошибка: курс {course} не в списке {control_list}'
        return person.set_grade(course, grade)
    
    def average_grade(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        return sum(grades)/max([len(grades), 1])

class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []

    def __str__(self):
        result = super().__str__()
        result += f'\nСредняя оценка за домашние задания: {self.average_grade()}'
        result += f'\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}'
        result += f'\nЗавершенные курсы: {', '.join(self.finished_courses)}'
        return result

    def set_grade(self, course, grade):
        return super().setgrade(course, grade, self.courses_in_progress)

    def rate_hw(self, lecturer, course, grade):
        return self.give_grade(lecturer, course, grade, Lecturer, self.finished_courses)

class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

class Lecturer(Mentor):
    def __str__(self):
        return super().__str__()+f'\nСредняя оценка за лекции: {self.average_grade()}'
    def set_grade(self, course, grade):
        return super().set_grade(course, grade, self.courses_attached)

class Reviewer(Mentor):
    def set_grade(self, course, grade):
        ...

    def rate_hw(self, student, course, grade):
        return self.give_grade(student, course, grade, Student, self.courses_attached)

def average_grade_persons(persons, course, control_type):
    grades = []
    for person in persons:
        if isinstance(person, control_type) and course in person.grades.keys():
            grades += person.grades[course]
    return sum(grades)/max([len(grades), 1])

def average_grade_lectoreres(lectoreres, course):
    return average_grade_persons(lectoreres, course, Lecturer)

def average_grade_strudents(students, course):
    return average_grade_persons(students, course, Student)

def load_data():
    for student in DATA['Students']:
        STUDENTS.append(Student(student[1], student[2], student[3]))
    for lectorer in DATA['Lectureres']:
        LECTURERES.append(Lecturer(lectorer[1], lectorer[2]))
    for reviwer in DATA['Reviwers']:
        REVIEWERS.append(Reviewer(reviwer[1], reviwer[2]))
    for course in DATA['Finished_courses']:
        STUDENTS[course[0]-1].finished_courses.append(DATA['Courses'][course[1]-1])
    for course in DATA['Courses_in_progress']:
        STUDENTS[course[0]-1].courses_in_progress.append(DATA['Courses'][course[1]-1])