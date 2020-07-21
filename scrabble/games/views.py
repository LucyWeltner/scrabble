from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Game, PlayerInGame, GameForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
	form = UserForm()
	return render(request, 'players/new.html', {"form": form})

def players_view(request):
	if request.method == "POST":
		data = UserForm(request.POST)
		if data.is_valid():
			name = data.cleaned_data.get("username")
			email = data.cleaned_data.get("email")
			password = data.cleaned_data.get("password")
			user = User.objects.create_user(name, email, password)
			player = Player.objects.create(user_id=user.id)
			return HttpResponse("<p>Player Successfully Created</p>")
		# return HttpResponseRedirect('/profile/')
		else:
			return HttpResponse("<p>There was an error, please try again</p>")

def login_view(request):
	if request.method == "POST":
		form =  authenticate.forms.AuthenticationForm()
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			return HttpResponseRedirect('/profile/')
		else: 
			return HttpResponse("<p>There was an error, please try again</p>")
	else:
		form = authenticate.forms.AuthenticationForm()
	render(request, 'players/login.html', {"form": form})




# def profile(request):


# def create_game(request):
	# newgame = (user1 = params[])
	#  = playerInGame(score=0, game=newgame, user=)




# meeting with Ben Kat - last step - tomorrow at 2 pm 
# Maybe technical questions 
# Steep learning curve 
# Trial contract with end date (6 months)
# values: ownership, inquisitiveness, ideas/innovation, someone who can grow with the business
