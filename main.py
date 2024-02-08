import django_setup
from school.models import Subject, Teacher, Class, Student


while True:
    choice=input('''
    Додавання предмету: 1
    Додавання вчителя: 2
    Додавання класу: 3
    Додавання учня: 4
    Вийти: 5
    ''')

    match choice:
        case '1':
            name = input('subject: ')
            subj = Subject(name=name).save()
        case '2':
            name = input('teacher name: ')
            subj = Subject.objects.get(name=input('subject name: '))
            teacher = Teacher(name=name)
            teacher.save()
            teacher.subject.add(subj)
        case '3':
            name = input('Class name: ')
            s_class = Class(name=name).save()
        case '4':
            name = input('Student name: ')
            s_class = Class.objects.get(name=input('class name: '))
            student = Student(name=name, school_class=s_class)
            student.save()
        case '5':
            exit()
