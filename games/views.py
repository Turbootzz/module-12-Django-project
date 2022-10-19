from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Games

# Create your views here.
def overview(request):
    games = Games.objects
    return render(request, 'games/games.html', {'games': games})


def detail(request, games_id):
    game = get_object_or_404(Games, pk=games_id)
    return render(request, 'games/detail.html', {'game': game})
