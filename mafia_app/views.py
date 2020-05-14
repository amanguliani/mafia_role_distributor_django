from django.shortcuts import render
from .models import Game
from .name_form import Players
from .game import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def new_game(request):
    created = False
    form = Players(request.POST or None)
    players_link_list = []
    if request.method == 'POST' and form.is_valid():
        names = []
        names.append("".join(form.cleaned_data['name_one'].lower().split()))
        names.append("".join(form.cleaned_data['name_two'].lower().split()))
        names.append("".join(form.cleaned_data['name_three'].lower().split()))
        names.append("".join(form.cleaned_data['name_four'].lower().split()))
        game_id = get_game_id()
        roles = get_ramdom_roles()
        for i in range(len(roles)):
            db = Game(person_name=names[i], game_name=game_id, role_assigned=roles[i])
            db.save()
            players_link_list.append(get_link(game_id, names[i]))
        created = True

    context = {
        'form': form,
        'created': created,
        'players_link_list': players_link_list
    }

    return render(request, 'new_game.html', context)

def player(request, game_id, player_name):
    player = Game.objects.get(person_name=player_name, game_name=game_id)
    context = {
        'role_image': '/static/images/' + player.role_assigned + '.png',
        'player_name': player_name,
        'player_role': player.role_assigned
    }
    return render(request, 'player.html', context)