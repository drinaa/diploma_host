from django.db import models
from django.contrib.auth.models import User

class reg_user(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

class professions(models.Model):
    name = models.CharField(max_length=30)

class points(models.Model):
    code = models.CharField(max_length=4)
    point = models.IntegerField()

class pupil(models.Model):
    pupil = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    doc_num = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    letter_grade = models.CharField(max_length=1)

class worker(models.Model):
    teach = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    mid_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=10)
    profession = models.ForeignKey(professions, on_delete=models.PROTECT)

class diplomas(models.Model):
    pupil = models.ForeignKey(pupil, on_delete=models.CASCADE)
    grade = models.IntegerField()
    year = models.IntegerField()
    name = models.CharField(max_length=100)
    nomination = models.CharField(max_length=25)
    type = models.IntegerField()
    level = models.IntegerField()
    place = models.IntegerField()
    part1 = models.IntegerField()
    part2 = models.IntegerField()
    point = models.IntegerField()