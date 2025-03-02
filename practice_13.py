# cylinder
class Cylinder:
    def __init__(self, radius, height, color):
        self.r = radius
        self.h = height
        self.color = color

    def calc_area(self, is_closed = True):
        if is_closed:
            area = 2 * 22/7 * self.r **2 + 2 * 22/7 * self.r * self.h
            print(f"The Area of a closed cylinder is: {area}")
        else:
            area = 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            print(f"The Area of an open cylinder is: {area}")
    def calc_volume(self):
        volume = 22 / 7 * self.r ** 2 * self.h
        print(f"The Volume of a cylinder is: {volume}")

# classes in python
# oop in python

c1 = Cylinder(5,7,"Blue")
c2 = Cylinder(9.5,20.4,"Red")
c1.calc_area(is_closed=False) # opened
c2.calc_volume()
c2.calc_area() # closed
c1.calc_volume()



