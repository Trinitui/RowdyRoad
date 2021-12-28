# Incorporate this:
# https://pygame-gui.readthedocs.io/en/latest/quick_start.html

from oak_island_fns import *
import time
from os import system, name
def oak_island():
    game = Depth()
    game_loop = True
    def clear():
  
        # for windows
        if name == 'nt':
            _ = system('cls')
  
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    
    while game_loop != False:
        while game.depth > 0:
            rate = 5
            game.passive_dig()
            print(f"You are digging at a rate of 1m every {rate}s")
            print(f'Current Depth: {1000 - game.depth}m')
            time.sleep(rate)
            clear()

        game_loop  = False