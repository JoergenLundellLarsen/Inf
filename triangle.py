import math
class Triangle:
    def __init__(self, top, left, right):
        self.t = top
        self.l = left
        self.r = right
        self.color = "green"
        self.linewidth = 2
        
    def color(self, color):
        self.color = color
    
    def set_linewidth(self, linewidth):
        self.linewidth = linewidth


    def draw(self, t):
        x1, y1 = self.t
        x2, y2 = self.l
        x3, y3 = self.r
        
        AB = math.sqrt((x2-x1)**2+(y2-y1)**2) #distance between the points
        BC = math.sqrt((x3-x2)**2+(y3-y2)**2)
        CA = math.sqrt((x1-x3)**2+(y1-y3)**2)
        
        A = math.degrees(math.acos((CA**2 + AB**2 - BC**2) / (2 * CA * AB)))
        B = math.degrees(math.acos((AB**2 + BC**2 - CA**2) / (2 * AB * BC)))
        C = 180 - A - B
        
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
        print(f"Triangle {self.t}, {self.l}, {self.r}, Area = {self.area():.2f} Color: {self.color}")
 