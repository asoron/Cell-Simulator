#cell.py
class Cell:
  def __init__(self, x,y,size,color):
    self.x = x
    self.y = y
    self.vx = 0
    self.vy = 0
    self.size = size
    self.color = color