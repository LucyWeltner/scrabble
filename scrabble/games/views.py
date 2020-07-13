from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Game, PlayerInGame
import datetime

def game_view(request):
	today = datetime.datetime.now().date()
	return render(request, 'games/index.html', {"today": today})

def new_game_view(request):
	players = Player.objects.all()
	playersobj = {}
	for num, player in enumerate(players, start=1):
		playersobj[num] = player
	print(playersobj)
	return render(request, 'games/new.html', {players: playersobj.values()})

# def create_game(request):
