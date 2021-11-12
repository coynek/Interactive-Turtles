from turtle import Turtle, ontimer 
import time
import os


class MovingTurtle(Turtle):
  def __init__(self, width, st, target = None):
    Turtle.__init__(self)
    self.width = width
    self.target = target
    self.st = st

    #  initial setup 
    self.shape("turtle")
    self.color("red")
    self.shapesize(3, 3, 1)
    self.penup()
    ontimer(self.move_self, 1)

    # variable
    self.x_spd = .5
    self.collision_distance = 15



  def move_self(self):
    target_angle = self.towards(self.target.xcor() , self.target.ycor())
    self.setheading(target_angle)
    
    self.forward(self.x_spd)
    if self.at_edge(): # returtn T or F
      self.x_spd = - self.x_spd
      pass # TODO -- finsih this
    ontimer(self.move_self, 1)
    if self.check_collision(self.target):
      endtime = time.time()
      finaltime = endtime - self.st
      self.checkfile(finaltime)
      quit()

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False

  def at_edge(self):
    if self.xcor() >= self.width/2 or self.xcor() < -self.width/2:
      return True
    else: 
      return False

  def checkfile(self, final):
    # read the current file
    file = open("highscore.txt", "r")
    score = file.read()
    file.close()
    if float(final) > float(score):
      os.remove("highscore.txt")
      file = open("highscore.txt", "w")
      file.write(str(final))
      file.close()
      