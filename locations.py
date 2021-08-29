import random,sys,time
from functions import combat, leave
from resources import enemies


def slow_type(t,wpm):
    
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)
    print('')

def normalize_text(txt):
  normal_text = txt.lower()
  return normal_text



def mansion(): 
  encounters = 0
  slow_type("Would you like to Enter the Dark Mansion?",90)
  x = normalize_text(input())

  if x != "no":
    slow_type("Welcome to the Dark Mansion!",90)
    slow_type("You will now be tested against the ghastly residents of this cursed Mansion!",90)
  else:
    slow_type("You slink away from the Dark mansion",90)
    leave()
  while encounters < 2:
    chosen = enemies[random.randint(0,len(enemies)-1)]
    slow_type(f"A {chosen[0]} appears!",50)
    combat(chosen[0],int(chosen[1]),int(chosen[2]))
    encounters += 1

  #Like -> combat("Zombie",random.randint(0,30),random.randint(40,50))
  print("what next.....")