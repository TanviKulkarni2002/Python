#Hill Cipher Algorithm (Decryption)
import numpy as np
word = []
x = str(input("Enter the string to be decrypted from Hill Cipher:\n"))
x1 = x.upper() 
x1 = x1.replace(" ","") 
for i in x1:
  k = ord(i) - 65
  word.append(k)
while(len(word)%3!=0):
  word.append(0)
n = len(word)//3 
word1 = np.array(word).reshape(3,n)
key = np.array([[8,5,10],[21,8,21],[21,12,8]]) #[[IFK],[VIV],[VMI]] chosen as the key matrix
def decrypt():
  ans = np.dot(key,word1)
  ans1 = (ans%26) #Taking mod 26
  ans2 = ans1.tolist()
  ans3 = []
  for l in ans2[0]:
    l = l + 65
    m = chr(l)
    ans3.append(m)
  for d in ans2[1]:
    d = d + 65
    n = chr(d) 
    ans3.append(n)
  for e in ans2[2]:
    e = e + 65
    o = chr(e)
    ans3.append(o)
  ans_f = "" 
  print("Decrypted string:")
  ans_f = ans_f.join(ans3)
  ans_f = ans_f.rstrip("A")
  print(ans_f)
decrypt()