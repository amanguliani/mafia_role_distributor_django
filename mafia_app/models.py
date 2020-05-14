from django.db import models

# Create your models here.
class Game(models.Model):
    person_name = models.CharField(max_length=30)
    game_name = models.CharField(max_length=30)
    role_assigned = models.CharField(max_length=30)