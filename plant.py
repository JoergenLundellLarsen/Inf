import math
import matplotlib.pyplot as plt

angle = 25
step = 3
depth = 5

#lagrer alle linjer som (x1, y1, x2, y2)
segments = []
stack = []

x, y = 0.0, -250.0
heading = 60 

def forward():
    global x, y
    rad = math.radians(heading)
    newx = x + step * math.cos(rad)
    newy = y + step * math.sin(rad)
    segments.append((x, y, newx, newy))
    x, y = newx, newy

def F(d):
    if d == 0:
        forward()
    else:
        F(d - 1)
        F(d - 1)

def X(d):
    global heading, x, y
    if d == 0:
        return
    F(d - 1)
    heading -= angle                     # -
    # [[X]+X]
    stack.append((x, y, heading))
    X(d - 1)
    heading += angle                     # +
    X(d - 1)
    if stack: x, y, heading = stack.pop()
    heading += angle                     # +
    F(d - 1)
    # [+FX]
    stack.append((x, y, heading))
    heading += angle                     # +
    F(d - 1)
    X(d - 1)
    if stack: x, y, heading = stack.pop()
    heading -= angle                     # -
    X(d - 1)

X(depth)

# plot resultatet
plt.figure(figsize=(8, 10), dpi=150)
for x1, y1, x2, y2 in segments:
    plt.plot([x1, x2], [y1, y2], color="green", linewidth=1)

plt.axis("equal")
plt.axis("off")
plt.show()
