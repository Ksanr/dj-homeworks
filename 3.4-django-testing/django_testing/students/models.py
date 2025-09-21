from django.conf import settings
from django.db import models


class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )

    def add_student(self, student):
        if self.students.count() >= getattr(settings, 'MAX_STUDENTS_PER_COURSE'):
            raise ValueError('Достигнут максимальный предел студентов на курсе')
        self.students.add(student)

    def __str__(self):
        return f'Course({self.id}, {self.name}, {self.students})'
