from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task, TaskDetails
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.
class TaskTest(TestCase):
    def setUp(self):
        self.type=Task(meetingtitle='Test Task')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Task')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'tasks')