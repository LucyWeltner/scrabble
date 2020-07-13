from django.shortcuts import render
from django.http import HttpResponse
import datetime

def game_view(request):
	today = datetime.datetime.now().date()
	return render(request, 'games/index.html', {"today": today})
