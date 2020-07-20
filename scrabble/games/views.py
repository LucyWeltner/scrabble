from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Game, PlayerInGame, GameForm, PlayerForm
import datetime

def game_view(request):
	today = datetime.datetime.now().date()
	games = Game.objects.all().order_by('name')
	if request.method == 'POST':
		form = GameForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get("name")
			player1 = form.cleaned_data.get("players")
			newgame = Game.objects.create(name=name)
			newgame.players.add(player1[0])
	return render(request, 'games/index.html', {"today": today, "games": games})

def new_game_view(request):
	form = GameForm()
	return render(request, 'games/new.html', {"form": form})
	# players = Player.objects.all()
	# playersArray = []
	# for player in players:
	# 	playersArray.append(player)
	# print(playersArray)
	# return render(request, 'games/new.html', {"players": playersArray})

def new_player_view(request):
	form = PlayerForm()
	return render(request, 'players/new.html', {"form": form})

def players_view(request):
	if request.method == "POST":
		data = PlayerForm(request.POST)
		if data.is_valid():
			name = data.cleaned_data.get("name")
			email = data.cleaned_data.get("email")
			password = data.cleaned_data.get("password")
			Player.objects.create(name=name, email=email, password=password)
			return render("<p>Player Successfully Created</p>")
		# return HttpResponseRedirect('/profile/')
	else:
		return render("<p>There was an error, please try again</p>")

# def create_game(request):
	# newgame = (user1 = params[])
	#  = playerInGame(score=0, game=newgame, user=)
