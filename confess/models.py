from django.db import models
from django.utils import timezone
# Create your models here.
class Confess(models.Model):
	to = models.CharField(max_length = 30)
	sender = models.CharField(max_length = 30)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	