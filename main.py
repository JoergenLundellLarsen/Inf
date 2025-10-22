from rectangle import Rectangle
from turtleplotlib import Turtle
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t = Turtle(interactive=False)

    shapes = (
        Rectangle((0, 0), (15, 10)),
        Rectangle((1, 3), (20, 25)),
        Rectangle((15, 30), (100, 200))
    )

    for rectangle in shapes:
        print(rectangle.info())
        rectangle.draw(t)

    plt.show()




    