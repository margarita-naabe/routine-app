from django.db import models
from django.db import models

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)


	def __str__(self, arg):
		return self.item + ' | ' + str(self.completed)
						

# Create your models here.


# Create your models here.
