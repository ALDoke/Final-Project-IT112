from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    tasktitle=models.CharField(max_length=255)
    taskduedate=models.DateField()
    tasklocation=models.TextField()

    def __str__(self):
        return self.tasktitle

    class Meta:
        db_table='tasks'

class TaskDetails(models.Model):
    taskid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    assignedperson=models.ManyToManyField(User)
    detailstext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.textid

    class Meta:
        db_table='taskdetails'