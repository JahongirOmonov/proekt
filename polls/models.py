from django.db import models
from datetime import datetime

# Create your models here.


class task(models.Model):
    taskname=models.CharField(max_length=190, default='')
    createAT=models.DateField(default=datetime.now)
    update=models.DateField(default=datetime.now)
    status=models.BooleanField(default=False)
    description=models.TextField(default='write here')

    def __str__(self) -> str:
        return self.taskname
