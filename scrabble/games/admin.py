from django.contrib import admin
from .models import Game
from .models import PlayerInGame
from .models import Player
# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
# admin.site.register(PlayerInGame)