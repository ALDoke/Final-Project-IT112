from django.contrib import admin
from .models import Task, TaskDetails
# Register your models here.
admin.site.register(Task)
admin.site.register(TaskDetails)