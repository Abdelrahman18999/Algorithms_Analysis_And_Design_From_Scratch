# Algorithm for calculate the Area of a circle
import math

def circle_area():
    radius = eval(input("Enter the radius of the circle: ")) # INPUT
    area = math.pi * (radius * radius)  # PROCESS
    return area

# OUTPUT
print("The Area of the cirlce = {}".format(circle_area()))
print("The Area of the cirlce = {}".format(circle_area()))