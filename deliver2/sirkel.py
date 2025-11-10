import math
import random
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
