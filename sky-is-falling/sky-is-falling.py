# sky is falling
# youtube tutorial: TokyoEdtech

import turtle
import random

wn = turtle.Screen()
wn.title("Falling Sky by lindsive")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# add the player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# add the good_guy
good_guy = turtle.Turtle()
good_guy.speed(0)
good_guy.shape("circle")
good_guy.color("blue")
good_guy.penup()
good_guy.goto(0, 250)
good_guy.direction = "stop"

# functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# keyboard binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    # Update screen
    wn.update()

    # move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
    
    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    # move the good_guy
    y = good_guy.ycor()
    y -= 3
    good_guy.sety(y)

    # check if good_guy is off screen
    if y < -300:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        good_guy.goto(x, y)

    # check for a collision with the player
    if good_guy.distance(player) < 20:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        good_guy.goto(x, y)

wn.mainloop()
