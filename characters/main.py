from .inventory import inventory
from .skill_tree import skill_tree

character_level = 1
character_class = ""
max_hp = 10
actual_hp = 10
stamine = 5

def _alter_character_hp(amount, type):
    global actual_hp, max_hp
    
    if type == 'heal':
        actual_hp = min(actual_hp + amount, max_hp)
    elif type == 'dmg':
        actual_hp = min(actual_hp + amount, 0) 