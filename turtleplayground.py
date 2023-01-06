from turtle import *

def reset_turtle():
  goto(0,0)

def random_shape(_speed, _distance, _angle):
  speed(_speed)
  
  for i in range(0,_distance):
    hideturtle()
    forward(_distance)
    right(_angle)
    forward(_distance)
    right(_angle)
    forward(_distance)
    right(_angle)
    forward(_distance)
    right(_angle)
    
    #Change _distance for different results
    _distance-=3


def pause():
  penup()
  for i in range(500):
    left(360)


def main():
  reset_turtle()
  speed=100
  distance=100
  angle=90
  random_shape(speed, distance, angle)
  reset_turtle()
  random_shape(speed, distance, -angle)
  speed=2
  pause()


main()