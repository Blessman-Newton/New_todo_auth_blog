from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Todo(models.Model):
	task = models.CharField(max_length=50)


	def __str__(self):
		return self.task


class Blog(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(default=datetime.now, blank=True)


	def __str__(self):
		return self.title



