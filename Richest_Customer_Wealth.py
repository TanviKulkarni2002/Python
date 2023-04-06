# i : Customer; j : Bank
import numpy as np
no_cust = int(input("Enter the number of customers: "))
no_bank = int(input("Enter the number of banks: "))

li = []
for i in range (0,no_cust):
    for j in range (0,no_bank):
        x = int(input("Enter the value: "))
        li.append(x)
mat = np.array(li).reshape(no_cust,no_bank)
print(mat)
final = 0
value = 0
for k in range (len(mat)):
    value = sum(mat[k])
    if(k+1<len(mat)):
        value2 = sum(mat[k+1])
    if value > final:
        if(value2>value):
            final = value2
        else:
            final = value
        print("The maximum wealth: ",final)
        break