# snake game
# youtube tutorial: TokyoEdtech

import turtle
import time
import random

delay = 0.1

# score
score = 0
score2 = 0
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

# snake head - player 1
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
head.goto(-100, 0)
# when starts it stops in middle
head.direction = "stop"

# snake head - player 2
head2 = turtle.Turtle()
# animation speed of turtle module - 0 is fastest
head2.speed(0)
# shape
head2.shape("square")
# color
head2.color("blue")
# doesn't draw
head2.penup()
# start at center of screen
head2.goto(100, 0)
# when starts it stops in middle
head2.direction = "stop"


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
segments2 = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Score2: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# game functions
# move up - player 1
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

# move snake head - player 1
def move():
   # move snake up
   if head.direction == "up":
      y = head.ycor()
      head.sety(y + 20)

   # move snake down
   if head.direction == "down":
      y = head.ycor()
      head.sety(y - 20)

   # move sneak left
   if head.direction == "left":
      x = head.xcor()
      head.setx(x - 20)

   # move snake right
   if head.direction == "right":
      x = head.xcor()
      head.setx(x + 20)

# ---------------------------------------------------

# player 2
# move up
def go_up2():
   if head2.direction != "down":
      head2.direction = "up"

# move down
def go_down2():
   if head2.direction != "up":
      head2.direction = "down"

# move left
def go_left2():
   if head2.direction != "right":
      head2.direction = "left"

# move right
def go_right2():
   if head2.direction != "left":
      head2.direction = "right"

# move snake head
# player 2
def move2():
   # move snake up
   if head2.direction == "up":
      y = head2.ycor()
      head2.sety(y + 20)

   # move snake down
   if head2.direction == "down":
      y = head2.ycor()
      head2.sety(y - 20)

   # move sneak left
   if head2.direction == "left":
      x = head2.xcor()
      head2.setx(x - 20)

   # move snake right
   if head2.direction == "right":
      x = head2.xcor()
      head2.setx(x + 20)


# keyboard bindings
# player 1
wn.listen()
# up arrow key
wn.onkeypress(go_up, "Up")
# down arrow key
wn.onkeypress(go_down, "Down")
# left arrow key
wn.onkeypress(go_left, "Left")
# right arrow key
wn.onkeypress(go_right, "Right")

# player 2
# up arrow key
wn.onkeypress(go_up2, "w")
# down arrow key
wn.onkeypress(go_down2, "s")
# left arrow key
wn.onkeypress(go_left2, "a")
# right arrow key
wn.onkeypress(go_right2, "d")

# main game loop
while True:

   # updates screen with each loop
   wn.update()

   # check for snake and border collision
   # player 1
   if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
      # one second pause befor egame starts again
      time.sleep(1)
      # reset position of head back to center
      head.goto(-100, 0)
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
      pen.write("Score: {}  Score2: {}  High Score: {}".format(
      score, score2, high_score), align="center", font=("Courier", 24, "normal"))

   # check for snake and border collision
   # player 2
   if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 290 or head2.ycor() < -290:
      # one second pause before game starts again
      time.sleep(1)
      # reset position of head back to center
      head2.goto(100, 0)
      # stops head frrom moving
      head2.direction = "stop"

      # hide the segments
      for segment in segments:
         segment.goto(1000, 1000)

      # clear the segments
      segments.clear()

      # reset score
      score2 = 0

      pen.clear()
      pen.write("Score: {} Score2: {}  High Score: {}".format(
          score, score2, high_score), align="center", font=("Courier", 24, "normal"))

   # check for collision between head and food
   # if the distance between the head and the food is 20:
   # player 1
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
      delay -= 0.001

      # increase the score
      score += 10

      if score > high_score:
         high_score = score
      elif score2 > high_score:
         high_score = score2

      pen.clear()
      pen.write("Score1: {},  Score2: {},   High Score: {}".format(
      score, score2, high_score), align="center", font=("Courier", 24, "normal"))

   # move the end segments first in reverse order
   for index in range(len(segments) - 1, 0, -1):
      x = segments[index-1].xcor()
      y = segments[index - 1].ycor()
      segments[index].goto(x, y)

   # move segment[0] to where the head is
   if len(segments) > 0:
      x = head.xcor()
      y = head.ycor()
      segments[0].goto(x, y)

# ---------------------------------------------------------------------

   # check for collision between head and food
   # if the distance between the head and the food is 20:
   # player 2
   if head2.distance(food) < 20:
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
      segments2.append(new_segment)

      # shorten the delay
      delay -= 0.001

      # increase the score
      score2 += 10

      if score > high_score:
         high_score = score
      elif score2 > high_score:
         high_score = score2

      pen.clear()
      pen.write("Score: {}  Score2: {}  High Score: {}".format(
         score, score2, high_score), align="center", font=("Courier", 24, "normal"))

   # move the end segments first in reverse order
   for index in range(len(segments2) - 1, 0, -1):
      x = segments2[index-1].xcor()
      y = segments2[index - 1].ycor()
      segments2[index].goto(x, y)

   # move segment[0] to where the head is
   if len(segments2) > 0:
      x = head2.xcor()
      y = head2.ycor()
      segments2[0].goto(x, y)


   move()
   move2()

   # check for head collision with the body segments
   # player 1
   for segment in segments:
      if segment.distance(head) < 20:
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
         delay = 0.1

         # update the score display
         pen.clear()
         pen.write("Score: {}  Score2: {}   High Score: {}".format(
         score, score2, high_score), align="center", font=("Courier", 24, "normal"))

         # ============================================================

   # check for head collision with the body segments
   # player 2
   for segment in segments2:
      if segment.distance(head2) < 20:
         time.sleep(1)
         head2.goto(0, 0)
         head2.direction = "stop"

         # hide the segments
         for segment in segments2:
            segment.goto(1000, 1000)

         # clear the segments
         segments2.clear()

         # reset score
         score2 = 0

         # reset the delay
         delay = 0.1

         # update the score display
         pen.clear()
         pen.write("Score: {}  Score2: {}  High Score: {}".format(
            score, score2, high_score), align="center", font=("Courier", 24, "normal"))


   time.sleep(delay)

# keeps window open
wn.mainloop()
