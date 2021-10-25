from turtle import Screen 
from clickableturtle import ClickableTurtle
window = Screen()
window.bgpic("turtle3.png")
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

start_button = ClickableTurtle("Start")



window.listen()
window.mainloop()

