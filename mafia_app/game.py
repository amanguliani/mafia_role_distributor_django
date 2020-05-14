import random
import string

def get_ramdom_roles():
    roles = ["King", "Minister", "Thief", "Police"]
    random.shuffle(roles)
    random.shuffle(roles)
    return roles

def get_game_id(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def get_link(gameid, name):
    return "player/" + gameid + "/" + name