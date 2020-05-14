from django.urls import path

from mafia_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_game', views.new_game, name='new_game'),
    path('player/<slug:game_id>/<slug:player_name>/', views.player, name='player'),
]
