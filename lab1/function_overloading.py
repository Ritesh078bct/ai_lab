from math import pi
class Shape:
    def area(self):
        return 0

class Rectange(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return pi*self.radius**2
    


rectangle=Rectange(4,5)
print(f"Reactangel area:{rectangle.area()}")
circle=Circle(3)
print(f"Circle Area:{circle.area():.2f}")