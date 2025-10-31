import random

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


