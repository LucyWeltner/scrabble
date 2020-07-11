from django.db import models

# Create your models here.
class Game(models.Model):
	totalScore = models.IntegerField()
	players = models.ManyToManyField(Player, through="PlayerInGame")