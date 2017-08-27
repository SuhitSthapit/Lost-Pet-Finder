from django.db import models

# Create your models here.
class LostPet (models.Model):
	name     = models.CharField(max_length=100, null=True, blank=True)
	type_pet = models.CharField(max_length=100, default='pet')
	age      = models.IntegerField(default='0')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.name   #objects are named as name of the pet in admin