import random
import time
import sys
import os
from features import Weapons, Items, Room, Food, Player, Enemy

os.system('cls')


intro = '''
You wake up in the middle of a forest wtih no recollection how you arrived. There appears to 
be a small makeshift camp. There is a what looks to be a shelter that should keep the elements
at bay. There is also a small firepit which looks to have gone out. To your south and west there
is a tall rock wall that isn't possible to climb. The only options are north and east. A faint
glow appears in the distance to the east. You can also some unknown animal sounds but aren't 
sure where they are coming from.
'''

manual = '''
Welcome to some game with a name
Available options are:
Move directions: north, east, south, west. Requires command to start with 'go'
Actions:
    attack: requires weapon type. ex. attack with spoon
    eat: requires food type. ex. eat worm
    take: requires item type. ex. take toothpaste
    inventory: displays current inventory
    combine: combines two items. ex. combine flashligth batttery. Creates a working light
    look: take a look at current surroundings

Thanks for playing
'''


random_takes = ['Good luck with that', 'I don\'t think you can take that', 'A valiant attempt', 'Not likely']

# Enemy list
worried_weasel = Enemy('worried weasel', 25, 15, 'sharp toenail', 'fiercly slobbering')
rabid_rabbit  = Enemy('rabid rabbit', 50, 15, 'rubber carrot', 'drooling and jumpng')
major_monkey = Enemy('major monkey', 100, 30, 'iron banana', 'hungry')

# Weapon list
sharp_spoon = Weapons('spoon', 'A rusty spoon with a sharpened edge', 15)

# Room list
room_one = Room(['south', 'west'], 'A room in Q1', ['spoon', 'rock'], (1,1), worried_weasel, None)
room_two = Room(['south', 'east'], 'A room in Q2', ['key', 'chest'], (1,0), rabid_rabbit, None)
room_three = Room(['north', 'east'], 'A room in Q3', ['bird'], (0,0), None, sharp_spoon)
room_four = Room(['north', 'west'], 'A room in Q4', ['cheese', 'map'], (0,1), major_monkey, None)



# Dictionary to hold rooms and their coordinates
room_dict = {(1,1): room_one, (1,0): room_two, (0,0): room_three, (0,1): room_four}

def intro_print(intro):
    for c in intro:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def battle(enemy):
    if player.weapon == []:
        print(f'You have no available weapons and have been killed by the {enemy.name}\'s {enemy.weapon}')
        player.health = 0

    else:
        while True:
            
            player.health -= enemy.attack
            print(f'{enemy.name} attacks {player.name}. {player.name}\'s health is {player.health}')
            time.sleep(1)
            if player.health <= 0:
                print(f'You have been killed by the {enemy.name} with their {enemy.weapon}')
                break
            # isn't bringing weapon class over
            enemy.health -= player.weapon[0].attack
            print(f'{player.name} attacks {enemy.name}. {enemy.name}\'s health is {enemy.health}')
            time.sleep(1)
            if enemy.health <= 0:
                print(f'You have killed the {enemy.name} with your {player.weapon[0].name}')
                current_room.enemy = None
                break
            
        
def eat(action):
    if any(x in action for x in inventory['food']):
        food = list(set(action) & set(inventory['food']))
        print(f'You have eaten {food[0]} your health is TBD')
        inventory['food'].remove(food[0])
    else:
        print('You can\'t eat that')

def take(item):
    # Item will be item in room. 
    if current_room.inventory == []:
        print('There are no available items in this room')

    elif item in current_room.inventory:
        player.inventory.append(item)
        current_room.inventory.remove(item)
        print(f'You have picked up the {item}')

    # picking up string not weapon
    elif item == current_room.weapon.name:
        player.weapon.append(current_room.weapon)
        print(f'You have picked up {player.weapon[0].name}')
        current_room.weapon = None

    elif item not in current_room.inventory:
        print('There aren\'t any of those in this room')
    else:
        print(random.choice(random_takes))

def drop(item):
    if player.inventory == []:
        print('You have no available items to drop. Except your pants. Don\'t even think about it')
    elif item in player.inventory:
        current_room.inventory.append(item)
        player.inventory.remove(item)
        print(f'You have dropped up the {item}')
    else:
        print('You don\'t have any of those')

def combine(action):
    # Function to combine two items
    pass

def room_desc(current_room):
    # Used to explain what's in a room after moving
    pass

def change_room(action, current_room):
    loc = list(current_room.location)
    if action not in current_room.exits:
        print('That direction is blocked')
    elif action == 'north':
        loc[0] += 1
    elif action == 'south':
        loc[0] -= 1
    elif action == 'west':
        loc[1] -= 1
    elif action == 'east':
        loc[1] += 1
    current_room = room_dict[tuple(loc)]
    print(current_room.desc)
    return current_room


#intro_print(intro)
current_room = room_three

name = input('What is your name? ')
player = Player(name)
print(current_room.desc)

while True:
    if player.health <= 0:
        game = input('Would you like to play again? y or n ')
        if game == 'y':
            player.health = 100
            os.system('cls')
        else:
            break

    action = (input('> ')).split(' ')

    if 'go' in action[0]:
        current_room = change_room(action[1], current_room)
    
    elif 'drop' in action[0]:
        drop(action[1])

    elif action[0] == 'inventory':
        if player.inventory == []:
            print('You are currently not carrying anything')
        else:
            print(f'You are currently carrying the following: {", ".join(player.inventory)}')

    elif action[0] == 'look':
        print(f'{current_room.desc} with items {", ".join(current_room.inventory)}')
        if current_room.enemy:
            print(f'There is also a {current_room.enemy.name} who is {current_room.enemy.mood} and seems to ready to attack')
        if current_room.weapon:
            print(f'there is also a {current_room.weapon.name} next to you')

    elif action[0] == 'take':
        take(action[1])

    elif action[0] == 'exits':
        print(f'Available exits are: {", ".join(current_room.exits)}')
    
    elif action[0] == 'attack':
        battle(current_room.enemy)
    
    elif action[0] == 'weapons':
        print(f'You are currently carrying {player.weapon.name}')

    elif action[0] == 'quit':
        break

    elif action[0] == 'help':
        print(manual)

    else:
        print('I don\'t understand that command')
    print('\n')
