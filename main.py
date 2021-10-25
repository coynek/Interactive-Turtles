from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from movingturtle import MovingTurtle
import time

# set up instance of the screen
window = Screen()
window.bgpic("grass.png")


screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance
button = ClickableTurtle()

#set up players
player_1 = KeyboardTurtle(window)

player_1.goto(100,100)

# set target of other player(our collison check) to the opposite player
starttime = time.time()
moveT = MovingTurtle(screen_width, starttime)
#player_1.other_player = moveT
moveT.target = player_1
# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment