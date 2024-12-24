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
    'Lectors': [
        [1, 'Сахиб', 'Болтонбаев'],
        [2, 'Мустафа', 'Хамраев'],
        [3, 'Тулкин', 'Ядыгханов'],
        [4, 'Равшан', 'Холмухаммедов']
    ],
    'Reviewers': [
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
    'Attached_courses_lectors': [
        [1, 1], [2, 1], [3, 2], [4, 2]
    ],
    'Lectors_grades': [
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
        [2, 3, 2, 9], [2, 4, 2, 6],
        [3, 3, 2, 7], [3, 4, 2, 2],
        [4, 3, 2, 5], [4, 4, 2, 10],
        [5, 3, 2, 8], [5, 4, 2, 9],
        [6, 1, 1, 9], [6, 2, 1, 6],
        [7, 1, 1, 10], [7, 2, 1, 8],
        [8, 1, 1, 2], [8, 2, 1, 3],
        [9, 1, 1, 10], [9, 2, 1, 4],
        [10, 1, 1, 4], [10, 2, 1, 10]
    ]
}

STUDENTS = []
LECTORS = []
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
            print(f'Ошибка: курс {course} не в списке {control_list}')
            return
        if grade not in range(MIN_GRADE, MAX_GRADE+1):
            print(f'Ошибка: оценка {grade} не входит в диапазон {MIN_GRADE}:{MAX_GRADE} у {self} за курс {course}')
            return
        if course in self.grades.keys():
            self.grades[course] += [grade]
        else:
            self.grades[course] = [grade]

    @staticmethod
    def give_grade(person, course, grade, control_type=None, control_list=None):
        if not isinstance(person, control_type):
            print(f'Ошибка: объект {person} не является экземпляром класса {control_type}')
            return
        if control_list is not None and course not in control_list:
            print(f'Ошибка: курс {course} не в списке {control_list}')
            return
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
        result += f'\nСредняя оценка за домашние задания: {self.average_grade():3.1f}'
        result += f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
        result += f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def set_grade(self, course1, grade, **kwargs):
        return super().set_grade(course1, grade, self.courses_in_progress)

    def rate_hw(self, lector, course, grade):
        return Person.give_grade(lector, course, grade, Lector, self.finished_courses)


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lector(Mentor):
    def __str__(self):
        return super().__str__()+f'\nСредняя оценка за лекции: {self.average_grade():3.1f}'

    def set_grade(self, course1, grade, **kwargs):
        return super().set_grade(course1, grade, self.courses_attached)


class Reviewer(Mentor):
    def set_grade(self, course1, grade, **kwargs):
        ...

    def rate_hw(self, student, course, grade):
        return Person.give_grade(student, course, grade, Student, self.courses_attached)


def average_grade_persons(persons, course, control_type):
    grades = []
    for person in persons:
        if isinstance(person, control_type) and course in person.grades.keys():
            grades += person.grades[course]
    return sum(grades)/max([len(grades), 1])


def average_grade_lectors(lectors, course):
    return average_grade_persons(lectors, course, Lector)


def average_grade_students(students, course):
    return average_grade_persons(students, course, Student)


def load_data():
    for student in DATA['Students']:
        STUDENTS.append(Student(student[1], student[2], student[3]))
    for lector in DATA['Lectors']:
        LECTORS.append(Lector(lector[1], lector[2]))
    for reviewer in DATA['Reviewers']:
        REVIEWERS.append(Reviewer(reviewer[1], reviewer[2]))
    for course in DATA['Finished_courses']:
        STUDENTS[course[0]-1].finished_courses.append(DATA['Courses'][course[1]-1][1])
    for course in DATA['Courses_in_progress']:
        STUDENTS[course[0]-1].courses_in_progress.append(DATA['Courses'][course[1]-1][1])
    for course in DATA['Attached_courses_lectors']:
        LECTORS[course[0]-1].courses_attached.append(DATA['Courses'][course[1]-1][1])
    for course in DATA['Attached_courses_reviewers']:
        REVIEWERS[course[0]-1].courses_attached.append(DATA['Courses'][course[1]-1][1])
    for grade in DATA['Lectors_grades']:
        STUDENTS[grade[0]-1].rate_hw(LECTORS[grade[1]-1], DATA['Courses'][grade[2]-1][1], grade[3])
    for grade in DATA['Students_grades']:
        REVIEWERS[grade[1]-1].rate_hw(STUDENTS[grade[0]-1], DATA['Courses'][grade[2]-1][1], grade[3])


def check_grade(grade):
    if grade == 1:
        return f'{grade:4.1f} балл'
    elif 1 < grade < 5:
        return f'{grade:3.1f} балла'
    else:
        return f'{grade:3.1f} баллов'


if __name__ == "__main__":
    load_data()
    best_student = max(STUDENTS)
    worse_student = min(STUDENTS)
    best_lector = max(LECTORS)
    worse_lector = min(LECTORS)
    print(
        f'Лучший студент:\n{best_student}',
        f'Отстающий студент:\n{worse_student}',
        f'Лучший лектор:\n{best_lector}',
        f'Отстающий лектор:\n{worse_lector}',
        sep='\n'
    )
    for dc in DATA['Courses']:
        print(
            f'Средняя оценка студентов курса "{dc[1]}" {check_grade(average_grade_students(STUDENTS, dc[1]))}.',
            f'Средняя оценка лекторов курса "{dc[1]}" {check_grade(average_grade_lectors(LECTORS, dc[1]))}.',
            sep='\n'
        )
