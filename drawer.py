from rectangle import Rectangle
from sirkel import Sirkel
from turtleplotlib import Turtle
import matplotlib.pyplot as plt

def draw_figures(color = "blue", linewidth = 2):
    t = Turtle(interactive=False)
    t.color(color)
    t.width(linewidth)
    
    r = 100 

    figurer = (
        Sirkel((0, 0), r, hjørner=180),
        Rectangle((-r, -r), (r, r)),                    
    )

    for figur in figurer:
        figur.info()
        figur.draw(t)

    plt.show()
    

