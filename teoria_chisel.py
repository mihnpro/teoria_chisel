import matplotlib.pyplot as plt
import numpy as np

arr1 = []
arr2 = []
arr3 = []
f = int(input())
suma = 0

def prosto(f):
    flag = 0
    for i in range(2, f):
        if f % i != 0:
            flag = 1
            break 
    if flag == 1:
        return(False)
    else:
        return(True)

        
while prosto(f) == False:
    suma = 0
    for i in range(1, f):
        if f % i == 0:
            suma += i
            print(i, "+", end = " ")

    f = suma
    arr1.append(f)
    print("=", f, "]]", end = " ")

l = len(arr1)
arr2 = [i for i in range(1, l+1)]


fig, ax = plt.subplots()             
ax.plot(arr2, arr1)  
plt.show()                           