from django.db import models

# Create your models here.

class Workout(models.Model):
	name = models.CharField(max_length=255)
	current_streak = models.IntegerField(default=0)
	longest_streak = models.IntegerField(default=0)
	color = models.CharField(max_length=128, default='green')

class Record(models.Model):
	workout = models.ForeignKey('Workout')
	count = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)

	def clean_date(self):
		month = int(self.date.strftime('%m'))
		day = int(self.date.strftime('%d'))
		return ''.join([str(month),'/',str(day)])
	
	clean = property(clean_date)




