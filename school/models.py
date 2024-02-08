from django.db import models

# Create your models here.


class Subject(models.Model):
    """name: str"""
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """name: str, subject: ManyToMany Subject"""
    name = models.CharField(max_length=50, unique=True)
    subject = models.ManyToManyField(Subject, related_name='teacher')

    def __str__(self):
        return self.name


class Class(models.Model):
    """name: str"""
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Student(models.Model):
    """name: str, school_class: ManyToMany Subject"""
    name = models.CharField(max_length=50)
    school_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name='student')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name='schedule')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name='schedule')
    school_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name='schedule')


class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)


