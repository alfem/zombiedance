
COORDS=((0,0),(222,0),(444,0),
        (0,222),(222,222),(444,222),
        (0,444),(222,444),(444,444))

class Player:
  """
     A Player
  """

  def __init__(self):
   self.cell=4
   self.move()
   self.kills=0
   self.lives=5
 
  def move(self):
   self.x=COORDS[self.cell][0]
   self.y=COORDS[self.cell][1]

