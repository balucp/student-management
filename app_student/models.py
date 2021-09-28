from django.db import models

TERM_CHOICES = ((1, 'One'), (2, 'Two'),(3, 'Three'))
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    teacher = models.ForeignKey(to=Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mark(models.Model):
    student = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    maths = models.PositiveIntegerField()
    science = models.PositiveIntegerField()
    history = models.PositiveIntegerField()
    term = models.PositiveSmallIntegerField(choices=TERM_CHOICES)
    total = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('student', 'term'))   
