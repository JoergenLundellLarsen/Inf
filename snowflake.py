from turtleplotlib import Turtle
import matplotlib.pyplot as plt
def snowflake(turtle, depth):
    if depth == 0:
        turtle.forward(8)          # utfør F
    else:                          # F ->
        snowflake(turtle, depth-1)  #      F
        turtle.left(60)             #        +
        snowflake(turtle, depth-1)  #          F
        turtle.right(60)            #            -
        turtle.right(60)            #              -  
        snowflake(turtle, depth-1)  #                F
        turtle.left(60)             #                  +
        snowflake(turtle, depth-1)  #                    F

t = Turtle(interactive=False)
for _ in range(3):
    snowflake(t, 3)
    t.right(120)
plt.show()
