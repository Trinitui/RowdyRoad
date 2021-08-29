class User:
  name = ''
  attack = 5
  defence = 5
  level = 1
  hp = 50
  def __init__(self,name):
    self.name = name
    self.attack = 10
    self.defence = 10
    self.level = 1
    self.hp = 50 
  def level_up(self,level):
    if self.level < 5:
      self.level += 1
      self.attack = self.attack + self.attack * 1.5
      self.defence = self.defence + self.attack*0.5
    else:
      self.level += 1
      self.attack += 5
      self.defence += 2.5
  def show_stats(self):
    a = self.level
    b = self.attack
    c = self.defence
    print(f"Level: {a}. Attack {b}. Defence {c}")
