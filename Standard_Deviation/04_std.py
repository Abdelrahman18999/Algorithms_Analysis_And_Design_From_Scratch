import math

# Declare my variables
array = []  # used for the data (sample)
sd = avg = a = b = 0  # avg __> average, a --> SUM(x[i] - avg)^2, b --> a / N

N = eval(input("Enter N = ")) # number of records

for i in range(0, N):
    record = eval(input("Enter array[{}] = ".format(i))) # take from user record by record.
    array.append(record) # append the enterd record from the user to our array.
    avg += record

avg = avg / N

for i in range(0, N):
    a += (array[i] - avg) ** 2

b = a / N

sd = math.sqrt(b)
print("Standard Deviation = {}".format(sd))