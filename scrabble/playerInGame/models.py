from django.db import models

# Create your models here.
class playerInGame(models.Model):
	game = models.ForeignKey(Game)
	player = models.ForeignKey(Player)
	score = models.IntegerField()
