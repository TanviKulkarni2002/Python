#Fiestal Structure Cipher
import math
str1 = input("Enter the string: ")
str1 = str1.upper() #Converts all lowercase letters to uppercase, if any
str1 = str1.replace(" ","")  #Removes all white spaces, if any
ascii_list = []
x = 0
y = 0
for i in str1:
    x = ord(i)
    ascii_list.append(x)
#print(ascii_list)

for i in range (0,len(ascii_list)):
    rem=""
    while ascii_list[i]>=1:
        rem+=str(ascii_list[i]%2)
        ascii_list[i]=math.floor(ascii_list[i]/2)

#Convert string to Binary 
binary=""
for i in range(len(rem)-1,-1,-1):
    binary = binary + rem[i]
bin_list = []
for i in binary:
    bin_list.append(i)
#print(bin_list)

#Divide into two parts of 4 bits each
L1 = []
R1 = []
l = len(bin_list)
if (l%2==0):
    for i in range (0,l/2):
        L1.append(int(bin_list[(i)]))
    for i in range (l/2 +1,l):
        R1.append(int(bin_list[int(i)]))
elif (l%2!=0):
    for i in range (0,math.ceil(l/2)):
        L1.append(int(bin_list[int(i)]))
    for i in range (math.ceil(l/2),l):
        R1.append(int(bin_list[int(i)]))
    if (len(R1)%2!=0):
        R1.insert(0,0)
    if (len(L1)%2!=0):
        L1.insert(0,0)
#print("LEFT SIDE: ",L1)
#print("RIGHT SIDE: ",R1)

#Fixed Keys K1 and K2 for two rounds
K1 = [1,1,1,0] 
K2 = [0,1,1,0]

F1 = []
F2 = []
R2 = []
L2 = R1
L3 = R2
R3 = []

#Enryption Rounds:
#Round 1A:
for i in range (0,4):
    r1 = R1[i] ^ K1[i]
    F1.append(r1)
#Round 1B:
for i in range (0,4):
    r2 = F1[i] ^ L1[i]
    R2.append(r2)
#Round 2A:
for i in range (0,4):
    r3 = R2[i] ^ K2[i]
    F2.append(r3)
#Round 2B:
for i in range (0,4):
    r4 = F2[i] ^ L2[i]
    R3.append(r4)

#Final List after two rounds
final_list = R3 + L3
#print(final_list)

#Convert binary to the equivalent ascii
encode_list = []
d = len(final_list)
for i in range (0,d):
    x = ((final_list[i]) * (2**(d-i)))%26 + 60
    X = chr(x)
    encode_list.append(X)
#print(encode_list)

encrypt = ''.join(encode_list)
print("Encrypted Word in Fiestal Structure Cipher: ",encrypt)