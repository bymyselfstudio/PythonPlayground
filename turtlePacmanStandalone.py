from turtle import *

def pause():
  hideturtle()
  penup()
  for i in range(100):
    left(360)


def pacman_body(stepsize):
  hideturtle()
  left(150)
  showturtle()
  pendown()
  fillcolor("yellow")
  begin_fill()
  forward(200)
  right(90)
  for i in range(300):
    forward(stepsize)
    right(1)
  right(90)
  forward(200)
  end_fill()
  penup()
  hideturtle()


def pacman_eye():
  goto(-80, 100)
  showturtle()
  pendown()
  dot(30, "black")


def main():
  # pen settings
  shape("arrow")
  pencolor("yellow")
  pensize(5)
  bgcolor("blue")
  speed(2)

  # draw pacman
  pacman_body(3.5)
  pacman_eye()
  pause()


main()
  