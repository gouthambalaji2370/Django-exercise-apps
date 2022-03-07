from django.db import models


# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=35)


class Passenger(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=35)
    rewardPoints = models.IntegerField()


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    salary = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=30)
    programmers = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=20)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Person(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField()


class License(models.Model):
    type = models.CharField(max_length=20)
    validFrom = models.DateField()
    validTo = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
