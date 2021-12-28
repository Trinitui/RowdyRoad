def oak_island_init():
    depth = 1000
    print(f'You use your radar to detect that treasure is at a depth of {depth}m')
    
    print("You see several digging implements around you...")

    print("Placeholder text!")

    return None
    

class Depth:
    dig = 0
    def __init__(self):
        self.depth = 1000

    def passive_dig(self):
        if self.dig < 5:
            self.depth -= 1
        else:
            self.depth -= self.dig * 1

    def advance_dig(self,dig):
        self.dig += 1

    def debug(self):
        print(
            self.depth,
            self.dig
        )

