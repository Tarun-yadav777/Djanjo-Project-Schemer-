from django.db import models


class Schemegen(models.Model):
    choices = [
        ("Women's Development", "Women's Development"),
        ("Social Justice", "Social Justice"),
        ("Sports", "Sports"),
        ("Ruler Development", "Ruler Development"),
        ("Child Development", "Child Development")
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=choices, default="Women's Development")
    info_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class User_info(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    dob = models.DateField(auto_now=False)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    interested_scheme = models.CharField(max_length=200)

    def __str__(self):
        return self.name
