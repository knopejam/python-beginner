# snake game - smooth version
# youtube tutorial: TokyoEdtech

import turtle
import time
import random

delay = 0.01

# score
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()
# title of screen
wn.title("Snake Game by lindsive")
# screen background color
wn.bgcolor("green")
# height and width of screennin px
wn.setup(width=600, height=600)
# turns off the screen updates
wn.tracer(0)

# snake head
head = turtle.Turtle()
# animation speed of turtle module - 0 is fastest
head.speed(0)
# shape
head.shape("square")
# color
head.color("black")
# doesn't draw
head.penup()
# start at center of screen
head.goto(0, 0)
# when starts it stops in middle
head.direction = "stop"
head.destination = (0, 0)

# snake food
food = turtle.Turtle()
# animation speed of turtle module - 0 is fastest
food.speed(0)
# shape
food.shape("circle")
# color
food.color("red")
# doesn't draw
food.penup()
# starting point
food.goto(0, 100)

# segments of body list
# next piece of body
segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Courier", 24, "normal"))

# game functions
# move up


def go_up():
    if head.direction != "down":
        head.direction = "up"

# move down


def go_down():
    if head.direction != "up":
        head.direction = "down"

# move left


def go_left():
    if head.direction != "right":
        head.direction = "left"

# move right


def go_right():
    if head.direction != "left":
        head.direction = "right"

# move snake head


def move():
    destination_x = head.destination[0]
    destination_y = head.destination[1]

    if head.xcor() < destination_x:
        head.setx(head.xcor() + 1)
    elif head.xcor() > destination_x:
        head.setx(head.xcor() - 1)
    elif head.ycor() > destination_y:
        head.sety(head.ycor() - 1)
    elif head.ycor() < destination_y:
        head.sety(head.ycor() + 1)
    # recalculate destination
    else:
        if head.direction == "up":
            destination_y += 20
        elif head.direction == "down":
            destination_y -= 20
        elif head.direction == "left":
            destination_x -= 20
        elif head.direction == "right":
            destination_x += 20

        head.destination = (destination_x, destination_y)


# keyboard bindings
wn.listen()
# up arrow key
wn.onkeypress(go_up, "Up")
# down arrow key
wn.onkeypress(go_down, "Down")
# left arrow key
wn.onkeypress(go_left, "Left")
# right arrow key
wn.onkeypress(go_right, "Right")

# main game loop
while True:

    # updates screen with each loop
    wn.update()

    # check for snake and border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # one second pause befor egame starts again
        time.sleep(1)
        # reset position of head back to center
        head.goto(0, 0)
        # stops head from moving
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments
        segments.clear()

        # reset score
        score = 0

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(
            score, high_score), align="center", font=("Courier", 24, "normal"))

    # check for collision between head and food
    # if the distance between the head and the food is 20:
    if head.distance(food) < 20:
        # move food to random spot of screen
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        # add a segment when snake collides with food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        # append new_segment to segment list
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.01

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(
            score, high_score), align="center", font=("Courier", 24, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment[0] to where the head is
    if len(segments) > 0:
        if segments[0].distance(head) == 20:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

    move()

    # check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 0:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments
            segments.clear()

            # reset score
            score = 0

            # reset the delay
            delay = 0.01

            # update the score display
            pen.clear()
            pen.write("Score: {}   High Score: {}".format(
                score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

# keeps window open
wn.mainloop()
