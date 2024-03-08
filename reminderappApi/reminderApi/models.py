from django.db import models
from datetime import datetime

# Create your models here.

class ReminderInfo(models.Model):

    date = models.DateField()
    time = models.TimeField()
    msg = models.TextField(max_length=1000)


    def  __str__(self):
        return str(self.date)
