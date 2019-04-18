from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    competition_date = models.DateTimeField()

