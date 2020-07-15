from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Game, PlayerInGame, GameForm, PlayerForm
import datetime

def game_view(request):
	today = datetime.datetime.now().date()
	return render(request, 'games/index.html', {"today": today})

def new_game_view(request):
	form = GameForm()
	return render(request, 'games/new.html', {"form": form})
	# players = Player.objects.all()
	# playersArray = []
	# for player in players:
	# 	playersArray.append(player)
	# print(playersArray)
	# return render(request, 'games/new.html', {"players": playersArray})

# def games_view(request):


# def create_game(request):
	# newgame = (user1 = params[])
	#  = playerInGame(score=0, game=newgame, user=)
