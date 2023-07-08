from django.db import models

class reserve(models.Model):
    name = models.CharField(max_length=100)
    time_field = models.TimeField()
    date_field = models.DateField()
    