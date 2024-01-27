import django_setup
from school.models import Subject, Teacher, Class, Student

subj = Subject(name='Math')
subj.save()

teache = Teacher(name='Lidia', subject=subj)
teache.save()
