# sky is falling
# youtube tutorial: TokyoEdtech

import turtle
import random
import os
import time

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Sky by lindsive")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("sky-is-falling/sky-falling-img/person_left.gif")
wn.register_shape("sky-is-falling/sky-falling-img/person_right.gif")
wn.register_shape("sky-is-falling/sky-falling-img/veggie.gif")
wn.register_shape("sky-is-falling/sky-falling-img/candy.gif")


# add the player
player = turtle.Turtle()
player.speed(0)
player.shape("sky-is-falling/sky-falling-img/person_left.gif")
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
    good_guy.shape("sky-is-falling/sky-falling-img/veggie.gif")
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
    bad_guy.shape("sky-is-falling/sky-falling-img/candy.gif")
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
    player.shape("sky-is-falling/sky-falling-img/person_left.gif")


def go_right():
    player.direction = "right"
    player.shape("sky-is-falling/sky-falling-img/person_right.gif")


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
        if good_guy.distance(player) < 40:
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
        if bad_guy.distance(player) < 40:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(
                score, lives), align="center", font=font)
            time.sleep(1)
            for bad_guy in bad_guys:
                bad_guy.goto(random.randint(-300, 300), random.randint(400, 800))

    # check for game over
    if lives == 0:
        pen.clear()
        pen.write("Game Over!  Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        time.sleep(5)
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives),
                align="center", font=("Courier", 24, "normal"))

wn.mainloop()
