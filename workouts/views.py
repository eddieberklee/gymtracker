# Create your views here.

# workouts/views.py

from django.http import HttpResponse
from django.shortcuts import render

from workouts.models import *

def index(request):
	workouts = Workout.objects.all()
	context = {
		'workouts': workouts,
	}
	template_name = 'index.html'
	return render(request, template_name, context)
	# return HttpResponse('index')






