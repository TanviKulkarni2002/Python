import numpy as np
from scipy import stats
ls = []
n = int(input("Enter the no of elements: "))
for i in range (0,n):
    x = float(input("Enter the element: "))
    ls.append(x)
print("Data entered: ",ls)

print("*** MENU ***\n1. Mean\n2. Median\n3. Mode")
choice = int(input("Enter your choice: "))
if(choice==1):
    sum = 0
    for i in ls:
        sum +=i
        ans = sum/len(ls)
    print("Mean of given data: ",ans)

elif(choice==2):
    ans = 0
    l = len(ls)
    if (l%2==0):
        ans = ((ls[int(l/2)]) + (ls[int(l/2) +1]))/2
    elif(len(ls)%2!=0):
        ans = ((ls[int(l/2)]))
    print("Median of given data: ",ans)

elif(choice==3):
    ans = stats.mode(ls)
    print("Mode of given data: ",ans)