
from rectangle import Rectangle
from sirkel import Sirkel
from triangle import Triangle
from turtleplotlib import Turtle
import matplotlib.pyplot as plt

def draw_figures(color = "blue", linewidth = 2):
    t = Turtle(interactive=False)
    r = 100 

    figurer = (
        Sirkel((0, 0), r, hjørner=180),
        Rectangle((-r, -r), (r, r)),     
        Triangle((0, r), (-r, -r), (r, -r))               
        )

    for figur in figurer:
        figur.info()
        t.color(figur.color)
        t.width(figur.linewidth)
        figur.draw(t)
        


        

    plt.show()
    

if __name__ == "__main__":
    draw_figures()

