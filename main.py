
from rectangle import Rectangle
from sirkel import Sirkel
from triangle import Triangle
from turtleplotlib import Turtle
import matplotlib.pyplot as plt

def draw_figures():
    t = Turtle(interactive=False)
    r = 100 
    figurer = (
        Sirkel((0, 0), r, hjørner=180),
        Rectangle((-r, -r), (r, r)),     
        Triangle((0, r), (-r, -r), (r, -r)),
        Sirkel((0, 0), 0.5*r, hjørner=180),
        Rectangle((-0.5*r, -0.5*r), (0.5*r, 0.5*r)),     
        Triangle((0, 0.5*r), (-0.5*r, -0.5*r), (0.5*r, -0.5*r)),
        Sirkel((0, 0), 0.25*r, hjørner=180),
        Rectangle((-0.25*r, -0.25*r), (0.25*r, 0.25*r)),     
        Triangle((0, 0.25*r), (-0.25*r, -0.25*r), (0.25*r, -0.25*r)),               
        )

    for figur in figurer:
        figur.info()
        figur.draw(t)
        

    plt.show()
    

if __name__ == "__main__":
    draw_figures()

