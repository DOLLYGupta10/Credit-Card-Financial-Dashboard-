from turtle import Screen, Turtle
import time
screen=Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("my snake game")

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

segments=[]
for position in STARTING_POSITION:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

    game_is_on = True
    while game_is_on:
      screen.update()
      time.sleep(0.1)

      for seg_num in range (start=2,stop=0,  )


