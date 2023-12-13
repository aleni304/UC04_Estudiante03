from django.db import models

class Course(models.Model):
    idcourse = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    hour = models.PositiveSmallIntegerField()
    credits = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=1)
    