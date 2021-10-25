from turtle import Turtle

class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,  
               straight = "Up", 
               turn_right = "Right",
               back = "Down",
               turn_left = "Left", 
               other_player = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.turn_right = turn_right
    self.back = back
    self.turn_left = turn_left
    self.other_player = other_player

    #set turtle starting states
    self.shape("turtle")
    self.color("light blue")
    self.penup()
    self.x_speed = 5 
    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_forward, self.straight)
    self.window.onkey(self.go_back, self.back)
    self.window.onkey(self.go_left, self.turn_left)


    #sets up controlling variables (y not implemented)
    self.movement_speed = 10
    self.turn_speed = 10
    self.collision_distance = 20

  # Movement Methods
  def go_forward(self):
    self.forward(self.movement_speed)
    if self.check_collision(self.other_player):
      print("crash")
      quit()
      
  def go_right(self):
    self.right(self.turn_speed)

  def go_back(self):
    self.forward(-self.movement_speed)
    if self.check_collision(self.other_player):
      print ("crash")
      quit()


  def go_left(self):
    self.left(self.turn_speed)

  # Useful Methods

  # This checks if object collides with another object.  
  # Right now it checks against the other player, but 
  # it doesn't NEED to.  It can check against any
  # other turtle object

  


    # TODO: finish setting up the inputs (left and down)
    
