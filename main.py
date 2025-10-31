from turtleplotlib import Turtle
import matplotlib.pyplot as plt
import math
import random

class Triangle:
    def __init__(self, top, left, right):
        self.t = top
        self.l = left
        self.r = right
        self.color = 'green'
        self.linewidth = 2

    def draw(self, t):
        colors = {
            "blue": "blue",
            "red": "red",
            "black": "black",
            "green": "green",
            "purple": "purple"
        }
        self.color = random.choice(list(colors.values()))
        self.linewidth = random.randint(1,5)
        x1, y1 = self.t
        x2, y2 = self.l
        x3, y3 = self.r
        
        AB = math.sqrt((x2-x1)**2+(y2-y1)**2) #distance between the points
        BC = math.sqrt((x3-x2)**2+(y3-y2)**2)
        CA = math.sqrt((x1-x3)**2+(y1-y3)**2)
        
        A = math.degrees(math.acos((CA**2 + AB**2 - BC**2) / (2 * CA * AB)))
        B = math.degrees(math.acos((AB**2 + BC**2 - CA**2) / (2 * AB * BC)))
        C = 180 - A - B
        
        t.color(self.color)
        t.width(self.linewidth)
        
        t.forward(AB)
        t.left(180-B)
        t.forward(BC)
        t.left(180-C)
        t.forward(CA)
        t.left(180-A)
    
    
    def area(self):
        x1, y1 = self.t
        x2, y2 = self.l
        x3, y3 = self.r
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

    def info(self):
        print(f"Triangle {self.t}, {self.l}, {self.r}, Area = {self.area():.2f} Color: {self.color} Linewidth: {self.linewidth}")
 
 
class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.ll = lower_left
        self.ur = upper_right
        self.color = "green"
        self.linewidth = 2

    def area(self):
        return (self.ur[0] - self.ll[0]) * (self.ur[1] - self.ll[1])

    def info(self):
        print(f"Rectangle Lower left: {self.ll} Upper right: {self.ur} Color: {self.color} Linewidth: {self.linewidth}")

    def draw(self, t):
        colors = {
            "blue": "blue",
            "red": "red",
            "black": "black",
            "green": "green",
            "purple": "purple"
        }
        self.color = random.choice(list(colors.values()))
        self.linewidth = random.randint(1,5)
        
        t.color(self.color)
        t.width(self.linewidth)

        x1, y1 = self.ll
        x2, y2 = self.ur
        width = x2 - x1
        height = y2 - y1

        t.up()              # for å ikke tegne fra sentrum til første punkt
        t.goto((x1, y1))
        t.down()                        
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)


class Sirkel:
    def __init__(self, sentrum, radius,hjørner=120):
        self.sentrum = sentrum
        self.radius = radius
        self.hjørner = hjørner
        self.color = "green"
        self.linewidth = 1
        

    def draw(self, t):
        colors = {
            "blue": "blue",
            "red": "red",
            "black": "black",
            "green": "green",
            "purple": "purple"
        }
        self.color = random.choice(list(colors.values()))
        self.linewidth = random.randint(1,5)
        t.color(self.color)
        t.width(self.linewidth)
        cx, cy = self.sentrum
        r = self.radius
        n = self.hjørner

        punkter = []
        for k in range(n):
            vinkel = 2 * math.pi * k / n
            x = cx + r * math.cos(vinkel)
            y = cy + r * math.sin(vinkel)
            punkter.append((x, y))

        #flytt til første punkt
        første_x, første_y = punkter[0]
        t.up()                      # for å ikke tegne fra sentrum til første punkt
        t.goto((første_x, første_y))
        t.down()

        #hele polygonet
        for (x, y) in punkter[1:]:
            t.goto((x, y))
        t.goto((første_x, første_y))  # Lukk sirkelen

    def area(self):
        return math.pi * self.radius ** 2

    def info(self):
        print(f"Sirkel med sentrum {self.sentrum}, radius {self.radius}, "
              f"hjørner {self.hjørner}, areal = {self.area():.2f} Color: {self.color} Linewidth: {self.linewidth}")

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

