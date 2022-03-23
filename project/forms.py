from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'