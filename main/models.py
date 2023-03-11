from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ForeignKey(Employee, blank=True, on_delete=models.DO_NOTHING)
