import random,sys,time
from user_class import User
from resources import enemies

player = User('')
time_count = 0

def normalize_text(txt):
  normal_text = txt.lower()
  return normal_text

def slow_type(t,wpm):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)
    print('')

def leave():
  return print("You leave the Dark Mansion")



def rowdy_road_init():
  
  slow_type("You set out on the Rowdy Road, a long and winding path through outer Newfoundland.",150)
  slow_type("There is but one goal - travel the Rowdy Road to its bitter end and achieve immortality by finding Captain Kidd's treasure at Oak Island.",150)

  slow_type("What is you name?",150)
  player = User(input())
  slow_type(f"Your journey begins now, {player.name}!",90)
  return player





def combat(enemy, enemy_hp, user_hp):
  speed = 110
  #print(player.show_stats())
  slow_type(f"You enter combat with {enemy}",speed)
  while enemy_hp > 0:
    #print(f"DEBUG, Enemy HP: {enemy_hp}, User HP: {user_hp}, is enemy over 0?{enemy_hp > 0}")
    slow_type("What action will you take?",speed)
    slow_type("1 for attack, 2 for dodge, 3 for escape",speed)
    action = input()
    if action == '1':
      dmg = random.randint(0,10)
      hurt = random.randint(0,10)
      slow_type(f"You do {dmg} damage to the {enemy}",speed)
      enemy_hp = enemy_hp - dmg
      user_hp = user_hp - hurt
      slow_type(f"The {enemy} does {hurt} damage!",speed)
      slow_type(f"you are now at {user_hp}HP, and the {enemy} is at {enemy_hp}HP",speed)
    if action == "2":
      slow_type("you attempt to dodge",speed)
      dodge_chance = random.randint(0,10)
      if dodge_chance > 4:
        slow_type(f"You dodged the {enemy}'s hellacious attack!'",speed)
        pass
      else:
        slow_type(f"The {enemy} attacks anyway!",speed)
        hurt = random.randint(0,10)
        user_hp = user_hp - hurt
        slow_type(f"you are now at {user_hp}",speed)
    if action == "3":
        dodge_chance = random.randint(0,10)
        if dodge_chance > 8:
            slow_type("You cannot escape!",speed)
            hurt = random.randint(0,10)
            user_hp = user_hp - hurt
            slow_type(f"you are now at {user_hp}",speed)
        else:
            return slow_type(f"You have escaped the {enemy}",speed)
    if user_hp <= 0:
      return slow_type("You have died",speed)
  if enemy_hp <= 0:
    return slow_type(f"You defeated the {enemy}",speed)