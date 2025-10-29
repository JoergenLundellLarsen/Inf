import math

class Sirkel:
    def __init__(self, sentrum, radius, hjørner=120):
        self.sentrum = sentrum
        self.radius = radius
        self.hjørner = hjørner

    def draw(self, t):
        cx, cy = self.sentrum
        r = self.radius
        n = self.hjørner

        punkter = []
        for k in range(n):
            vinkel = 2 * math.pi * k / n
            x = cx + r * math.cos(vinkel)
            y = cy + r * math.sin(vinkel)
            punkter.append((x, y))

        # Flytt til første punkt
        første_x, første_y = punkter[0]
        t.goto((første_x, første_y))

        # Tegn hele polygonet
        for (x, y) in punkter[1:]:
            t.goto((x, y))
        t.goto((første_x, første_y))  # Lukk sirkelen

    def area(self):
        return math.pi * self.radius ** 2

    def info(self):
        print(f"Sirkel med sentrum {self.sentrum}, radius {self.radius}, "
              f"hjørner {self.hjørner}, areal = {self.area():.2f}")
