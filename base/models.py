from django.db import models

# Create your models here.


class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    

class HistoryModel(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)