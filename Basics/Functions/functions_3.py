import math

def circle_rad (radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_rad(3)

print("Area is", a, "circumference is", c)

