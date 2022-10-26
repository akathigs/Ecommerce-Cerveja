from django.db import models

class produto(models.Model):
    nameProd = models.CharField(max_length=30)
    values = models.FloatField(max_length=30)
    mls = models.models.FloatField(max_length=5)

class user(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    username = models.FloatField(max_length=30)