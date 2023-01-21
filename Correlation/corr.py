import math

# declare variables
array1 = []
array2 = []
a = []
b = []
a_square = []
b_square = []
ab = []
corr = avg1 = avg2 = a_square_sum = b_square_sum = ab_sum = 0

N = eval(input("Enter N = "))

for i in range(0, N):
    
    a_inputs = eval(input("Enter array1[{}]: ".format(i)))
    array1.append(a_inputs)
    
    b_inputs = eval(input("Enter array2[{}]: ".format(i)))
    array2.append(b_inputs)
    
    avg1 += array1[i]
    avg2 += array2[i]
    
avg1 = avg1 / N
avg2 = avg2 / N

for i in range(0, N):
    a.append(array1[i] - avg1)
    b.append(array2[i] - avg2)
    
    a_square.append(a[i] ** 2)
    b_square.append(b[i] ** 2)
    
    ab.append(a[i] * b[i])
    
    a_square_sum += a_square[i]
    b_square_sum += b_square[i]
    ab_sum += ab[i]
    
corr = ab_sum / math.sqrt(a_square_sum * b_square_sum)

if corr >= 0.5:
    state = 'Strong Positive'
elif (corr < 0.5) and (corr > 0):
    state = 'Weak Positive'
elif corr > -0.5 :
    state = 'Weak Negative'
else:
    state = 'Strong Negative'

print("Correlation = {} and it is {}".format(corr, state))