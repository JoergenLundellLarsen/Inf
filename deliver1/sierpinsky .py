#Peder Hetland Flaat 
#Jørgen Lundell Larsen

from turtleplotlib import Turtle
import matplotlib.pyplot as plt


def sierpinskyA(t, depth, step):
    #Rule A → B - A - B
    if depth == 0:
        t.color("blue")
        t.forward(step)
    else:
        sierpinskyB(t, depth - 1, step) # (B)
        t.right(60)        # - = høyre
        sierpinskyA(t, depth - 1, step)
        t.right(60)        # - = høyre
        sierpinskyB(t, depth - 1, step) #(A)


def sierpinskyB(t, depth, step):
    #B → A + B + A
    if depth == 0:
        t.color("red")
        t.forward(step)
    else:
        sierpinskyA(t, depth - 1, step)
        t.left(60)         # '+' = venstre
        sierpinskyB(t, depth - 1, step)
        t.left(60)         # '+' = venstre
        sierpinskyA(t, depth - 1, step)


def sierpinsky_curve(t, depth=5, step=10):
    sierpinskyA(t, depth, step)
    plt.axis("equal")
    plt.axis("off")
    plt.show()


t = Turtle(interactive=False)
sierpinsky_curve(t, depth=6, step=12)
