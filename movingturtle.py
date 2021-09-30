from turtle import Turtle, ontimer 


class MovingTurtle(Turtle):
  def_init_(self, width):
    Turtle.__init__(self)
    self.width = width

    #  initial setup 
    self.shape("circle")
    self.shapesize(.5, .5, 1)
    self.penup()
    ontimer(self.move_self, 1)

    # variable
    self.x_spd = 4 

def move_self(self):
  self.forward(self.x_spd)
  if self.at_edge(): # returtn T or F
    self.x_spd = - self.x_speed
    pass # TODO -- finsih this
  ontimer(self.move_self, 1):

def at_edge(self):
  if self.xcor() >= self.width/2: or self.xcore < -seff.width/2:
    return True
  else: 
    return False: 