
from django.db import models

# Create your models here.
class Nurse(models.Model):
    LANGUAGE_CHOICES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ]

    nurse_id = models.AutoField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    experience = models.IntegerField()
    language = models.CharField(max_length=10, choices = LANGUAGE_CHOICES)
    qualification = models.CharField(max_length=200, default="")
    cv = models.FileField(upload_to="nurse/doc")
