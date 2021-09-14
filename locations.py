import random,sys,time
from functions import combat, leave
from resources import enemies
from textblob import TextBlob

time_count = 0
miles = 0
max_miles = 1000

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
    return leave()
  while encounters < 2:
    chosen = enemies[random.randint(0,len(enemies)-1)]
    slow_type(f"A {chosen[0]} appears!",50)
    combat(chosen[0],int(chosen[1]),int(chosen[2]))
    encounters += 1

  #Like -> combat("Zombie",random.randint(0,30),random.randint(40,50))
  print("what next.....")

def car_adventure(miles):
    slow_type(random.randint(1,10)*"*",40)
    miles += random.randint(0,9) * 100
    slow_type(f"You are now {miles - max_miles} miles from Oak Island",90)
    while miles < max_miles:
        slow_type(random.randint(1,10)*"*",90)
        miles += random.randint(0,9) * 100
    slow_type('You have arrived at Oak Island!',90)



def roadside():
    slow_type('You find a car by the side of the road',90)
    slow_type('What will you do?',90)
    res = input()
    print(TextBlob(res).sentiment.polarity)
    if TextBlob(res).sentiment.polarity > 0.25:
        slow_type('You take the car',90)
        car_adventure(max_miles)
    else:
        print("You face your deepest fear!")
        chosen = enemies[random.randint(0,len(enemies)-1)]
        slow_type(f"A {chosen[0]} appears!",50)
        combat(chosen[0],int(chosen[1]),int(chosen[2]))
        return None













def ongoing():
    while time_count < 100:
        flip = random.randint(1,10)
        print(flip)
        if flip > 9:
            mansion()
        if flip > 5 or flip <= 9:
            roadside()
        if flip == 5:
            pass
        else:
            print("You walk down the road...")