from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name='teacher')

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    school_class = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name='student')

    def __str__(self):
        return self.name
