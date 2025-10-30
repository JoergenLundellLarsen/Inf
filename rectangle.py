

class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.ll = lower_left
        self.ur = upper_right
        

    def area(self):
        return (self.ur[0] - self.ll[0]) * (self.ur[1] - self.ll[1])

    def info(self):
        print(f"Rectangle Lower left: {self.ll} Upper right: {self.ur}")

    def draw(self, t):
        x1, y1 = self.ll
        x2, y2 = self.ur
        width = x2 - x1
        height = y2 - y1

        t.goto((x1, y1))

        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

a = Rectangle((0, 0), (10, 5))
