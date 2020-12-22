# sky is falling
# youtube tutorial: TokyoEdtech

import turtle
import random

score = 0
lives = 3

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

# a list of good_guys
good_guys = []

# add the good_guys
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(100, 250)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)

# a list of bad_guys
bad_guys = []

# add the bad_guys
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("circle")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(0, 250)
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)

# make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.direction = "stop"
font = ("Courier", 24, "normal")
pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)

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

    # move the good_guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
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
            score += 10
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(
                score, lives), align="center", font=font)

    # move the bad_guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # check if bad_guy is off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # check for a collision with the player
        if bad_guy.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(
                score, lives), align="center", font=font)

wn.mainloop()
