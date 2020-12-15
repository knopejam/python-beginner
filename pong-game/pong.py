import turtle

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
border_sound_path = os.path.join(dir_path, 'bounce.wav')
paddle_sound_path = os.path.join(dir_path, 'paddle.wav')

wn = turtle.Screen()
wn.title("Pong by lindsive")
wn.bgcolor("orange")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball 1
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# move ball on x axis
ball.dx = .25
# move ball on y axis
ball.dy = -.25

# ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("white")
ball2.penup()
ball2.goto(0, 0)
# move ball on x axis
ball2.dx = -.25
# move ball on y axis
ball2.dy = -.25

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player a: 0  player b: 0", align="center", font=("Courier", 24, "normal"))

# functions
def paddle_a_up():
   y = paddle_a.ycor()
   y += 20
   paddle_a.sety(y)

def paddle_a_down():
   y = paddle_a.ycor()
   y -= 20
   paddle_a.sety(y)

def paddle_b_up():
   y = paddle_b.ycor()
   y += 20
   paddle_b.sety(y)

def paddle_b_down():
   y = paddle_b.ycor()
   y -= 20
   paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
   wn.update()

   # move the ball
   # .xcor() is current x axis position
   # .dx is moving the ball by 2 pixels
   # .ycor() is current y axis position
   # .dy is moving the ball by 2 pixels
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)

   # ball 2
   ball2.setx(ball2.xcor() + ball2.dx)
   ball2.sety(ball2.ycor() + ball2.dy)

   # border checking - ball 1
   # top border
   if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      os.system('afplay "{}"&'.format(border_sound_path))

   # bottom border
   if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      os.system('afplay "{}"&'.format(border_sound_path))
   
   # right border
   if ball.xcor() > 390:
      ball.goto(0, 0)
      ball.dx *= -1
      score_a += 1
      pen.clear()
      pen.write("player a: {}  player b: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
      os.system('afplay "{}"&'.format(border_sound_path))
   
   # left border
   if ball.xcor() < -390:
      ball.goto(0, 0)
      ball.dx *= -1
      score_b += 1
      pen.clear()
      pen.write("player a: {}  player b: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
      os.system('afplay "{}"&'.format(border_sound_path))

   # border checking - ball 2
   # top border
   if ball2.ycor() > 290:
      ball2.sety(290)
      ball2.dy *= -1
      os.system('afplay "{}"&'.format(border_sound_path))

   # bottom border
   if ball2.ycor() < -290:
      ball2.sety(-290)
      ball2.dy *= -1
      os.system('afplay "{}"&'.format(border_sound_path))

   # right border
   if ball2.xcor() > 390:
      ball2.goto(0, 0)
      ball2.dx *= -1
      score_a += 1
      pen.clear()
      pen.write("player a: {}  player b: {}".format(score_a, score_b),
               align="center", font=("Courier", 24, "normal"))
      os.system('afplay "{}"&'.format(border_sound_path))

   # left border
   if ball2.xcor() < -390:
      ball2.goto(0, 0)
      ball2.dx *= -1
      score_b += 1
      pen.clear()
      pen.write("player a: {}  player b: {}".format(score_a, score_b),
         align="center", font=("Courier", 24, "normal"))
      os.system('afplay "{}"&'.format(border_sound_path))

   # paddle and ball collisions - ball 1
   if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
      ball.setx(340)
      ball.dx *= -1
      os.system('afplay "{}"&'.format(paddle_sound_path))

   if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
      ball.setx(-340)
      ball.dx *= -1
      os.system('afplay "{}"&'.format(paddle_sound_path))
   
   # paddle and ball collisions - ball 2
   if (ball2.xcor() > 340 and ball2.xcor() < 350) and (ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() - 40):
      ball2.setx(340)
      ball2.dx *= -1
      os.system('afplay "{}"&'.format(paddle_sound_path))

   if (ball2.xcor() < -340 and ball2.xcor() > -350) and (ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() - 40):
      ball2.setx(-340)
      ball2.dx *= -1
      os.system('afplay "{}"&'.format(paddle_sound_path))

   # AI player
   if ball.xcor() > ball2.xcor():
      if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
         paddle_b_up()
      elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
         paddle_b_down()
   else:
      if ball.xcor() < ball2.xcor():
         if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
            paddle_b_up()
         elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
            paddle_b_down()
