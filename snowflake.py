from turtleplotlib import Turtle
import matplotlib.pyplot as plt

def snowflake(turtle, depth, step):
    if depth == 0:
        turtle.forward(step)
    else:
        snowflake(turtle, depth - 1, step)
        turtle.left(60)
        snowflake(turtle, depth - 1, step)
        turtle.right(120)
        snowflake(turtle, depth - 1, step)
        turtle.left(60)
        snowflake(turtle, depth - 1, step)

def complete_flake(t, depth=3, step=8):
    for _ in range(3):
        snowflake(t, depth, step)
        t.right(120)
    plt.show()

t = Turtle(interactive=False)
complete_flake(t, depth=3, step=3) 
