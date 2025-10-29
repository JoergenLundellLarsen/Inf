from rectangle import Rectangle
from sirkel import Sirkel
from turtleplotlib import Turtle
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t = Turtle(interactive=False)

    r = 100 

    figurer = (
        Sirkel((0, 0), r, hjørner=180),
        Rectangle((-r, -r), (r, r)),                    
    )

    for figur in figurer:
        figur.info()
        figur.draw(t)

    plt.show()
