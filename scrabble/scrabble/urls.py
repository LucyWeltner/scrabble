"""scrabble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from games.views import game_view, new_game_view, new_player_view, players_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', game_view, name='games'),
    path('games/new', new_game_view, name='new_game'),
    path('players/new', new_player_view, name='new_player'),
    path('players/', players_view, name='players'),
    path('login/', login_view, name='login')

]
