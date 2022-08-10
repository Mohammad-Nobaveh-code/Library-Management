from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
	CHOICES_OBJECT = (
		('M', 'male'),
		('F', 'female'),
	)
	age = models.PositiveIntegerField()
	phone_number = models.CharField(max_length=30)
	gender = models.CharField(max_length=1, choices=CHOICES_OBJECT)
	address = models.TextField()
	national_code = models.CharField(max_length=12)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	debt = models.OneToOneField('loan.Debt', on_delete=models.PROTECT)

	def __str__(self):
		return f'{self.user.username}'
