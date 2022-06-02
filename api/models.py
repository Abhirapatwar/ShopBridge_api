from django.db import models

class Entries(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    type=models.CharField(max_length=100)
    desc=models.CharField(max_length=150)

    