import random
from user_class import User
enemies = [["Zombie", random.randint(0, 30),
            User.hp],
           ["Cursed Bat",
            random.randint(0, 20),
            User.hp],
           ["The Devil",
            random.randint(0, 100),
            User.hp],
           ["Hell Hound",
            random.randint(0, 2),
            User.hp]]
