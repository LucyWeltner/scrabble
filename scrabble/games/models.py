from django.db import models
from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
	totalScore = models.IntegerField(default=0)
	players = models.ManyToManyField("Player", through="PlayerInGame")
	name = models.CharField(max_length=1000, verbose_name="what's the name of the game?")

	def __str__(self):
		return self.name

class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# name = models.CharField(max_length=200)
	# email = models.EmailField()
	# password = models.CharField(max_length = 200)
	games = models.ManyToManyField(Game, through="PlayerInGame")

	def __str__(self):
		return self.name

class PlayerInGame(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	
class GameForm(ModelForm):
	class Meta:
		model = Game
		fields = ['name', 'players']

class UserForm(ModelForm):
	password = CharField(widget=PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password']