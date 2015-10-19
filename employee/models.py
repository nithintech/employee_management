from django.db import models
from datetime import date


class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return "{}". format(self.name)

    def age(self):
        days_in_year = 365.2425
        age = int((date.today() - self.dob).days / days_in_year)
        return age


class Qualification(models.Model):
    employee = models.ForeignKey(Employee)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    pass_out_year = models.IntegerField()

    def __str__(self):
        return "{} - {} - {} - {}". format(self.employee, self.course, self.branch, self.pass_out_year)
