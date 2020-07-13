from django.db import models

# Create your models here.
class Game(models.Model):
	totalScore = models.IntegerField(default=0)
	players = models.ManyToManyField("Player", through="PlayerInGame")
	name = models.TextField(help_text="Enter a name for this game")

	def __str__(self):
		return self.name

class Player(models.Model):
	name = models.TextField(help_text= "Enter Your Username: ")
	email = models.EmailField(help_text= "Enter Your Email")
	games = models.ManyToManyField(Game, through="PlayerInGame")

	def __str__(self):
		return self.name

class PlayerInGame(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	
