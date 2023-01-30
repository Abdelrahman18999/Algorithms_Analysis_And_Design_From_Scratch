# INPUTS
N = eval(input("How many number/element do youu want ? "))
array = []

for number in range(N):
    array.append(eval(input("Enter element {} : ".format(number))))

# PROCESS
for i in range(1, len(array)):
    
    key = array[i]
    j = i - 1
    
    while (j >= 0):
        if key < array[j] :
            array[j+1] = array[j]
            j -= 1
        else :
            break
        
        
    array[j+1] = key
        
print("The sorted array is : {}".format(array))