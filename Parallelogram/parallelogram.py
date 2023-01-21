# INPUTS
base = eval(input("Enter How long the base? "))
height = eval(input("Enter How long the heigh? "))

# PROCESS
def parallelogramArea(base, height):
    parallelogram_area = base * height
    return parallelogram_area

# OUTPUT
print("The Area of Parallelogram = {}".format(parallelogramArea(base, height)))