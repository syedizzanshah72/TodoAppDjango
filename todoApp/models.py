from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    choice = [('l','low'),
              ('m','medium'),
              ('h','high')
              ]
    tasktitle = models.TextField(max_length=500)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField()
    priority = models.TextField(max_length=1,choices=choice)
    def __str__(self):
        return self.tasktitle

  