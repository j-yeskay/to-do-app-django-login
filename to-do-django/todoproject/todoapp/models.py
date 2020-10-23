from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ToDoItem(models.Model):
    task = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return str(self.task)

    def get_absolute_url(self):
        return reverse ('home')
