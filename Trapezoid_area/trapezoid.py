# INPUTS
smaller_base = eval(input("Enter the smaller base: "))
larger_base = eval(input("Enter the larger base: "))
height = eval(input("Enter the height: "))

# PROCESS
trapezoid_area = ((smaller_base + larger_base) / 2) * height

# OUTPUT
print("The Area of Trapezoid = {}".format(trapezoid_area))