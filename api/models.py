from django.db import models


class Patient(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=300)
    focusTime = models.IntegerField()
    password = models.CharField(max_length=100)
    no_of_test_attempts = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.age}"


class FocusCheck(models.Model):
    age_start = models.IntegerField()
    age_end = models.IntegerField()
    range_start = models.IntegerField()
    range_end = models.IntegerField()

    def __str__(self):
        return f"{self.age_start} {self.range_start} {self.range_end}"
