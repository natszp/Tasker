from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    importance = models.BooleanField(default=True, choices=IMPORTANT)

