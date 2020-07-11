from django.db import models

class Player(models.Model):
	name = models.TextField(help_text: "Enter Your Username: ")
	email = models.EmailField(help_text: "Enter Your Email")
	games = models.ManyToManyField(Game, through="playerInGame")
# Create your models here.
