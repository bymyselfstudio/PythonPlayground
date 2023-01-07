from turtle import *

bgcolor("black")
pencolor("white")

def reset_turtle():
  penup()
  goto(-150,150)
  pendown()


def random_shape(drawspeed, distance, angle):
  speed(drawspeed)
  for i in range(0, distance):
    hideturtle()
    for j in range(3):
      forward(distance)
      right(angle)
    distance-=2 # Change _distance for different results

    if distance <= 0:
      penup()
      break
    

def pause():
  penup()
  for i in range(500):
    left(360)


def main():
  reset_turtle()
  drawspeed=100
  distance=250
  angle=89
  random_shape(drawspeed, distance, angle)
  reset_turtle()
  speed=2
  pause()


main()