from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
	title=models.CharField(max_length=50)
	description=models.CharField(max_length=300)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	created_on=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.tilte

# Create your models here.
