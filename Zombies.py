import random

COORDS=((0,0),(222,0),(444,0),
        (0,222),(222,222),(444,222),
        (0,444),(222,444),(444,444))

class Zombie:
  """
     A Zombie, buried (at this momment) :-)
  """

  def __init__(self,where):
#   self.cell=random.choice((0,1,2,3,5,6,7,8))
   self.cell=where
   self.x=COORDS[self.cell][0]
   self.y=COORDS[self.cell][1]
   self.depth=-1
   self.type=0
#   self.type=random.randint(1)
   print self.cell,self.x,self.y,self.type

 
  def move(self):
    self.depth+=1

  def kill(self):
    self.depth=-1
