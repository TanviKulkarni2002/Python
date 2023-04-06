# Hill Cipher Algorithm (Encryption)
import numpy as np
word = []
x = str(input("Enter the word to be encrypted into Hill Cipher:\n"))
x1 = x.upper()
x1 = "".join(x1.split()) 
for i in x1:
  k = ord(i) - 65
  word.append(k)
while(len(word)%3!=0): 
  word.append(0)
n = len(word)//3 
word1 = np.array(word).reshape(3,n) 
key = np.array([[6,24,1],[13,16,10],[20,17,15]]) #[[GYB],[NQK],[URP]] chosen as the key matrix
def encrypt():
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
  print("Encrypted Word Formed:")
  ans_f = ans_f.join(ans3)
  print(ans_f)
encrypt()