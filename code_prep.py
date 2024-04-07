# a=[11, 12, 13, 14]
# b=[15, 16, 17, 18]
# def swap(a,b):
#     print("Before Swapping: ",a,b)
#     for i in range (0,len(a)):
#         temp=a[i]
#         a[i]=b[i]
#         b[i]=temp
#     print("After Swapping: ",a,b)
#     return
# swap(a,b)
# **************************************

# string="prepbytes"
# def sort_string(string):
#     ls=[]
#     for i in string:
#         ls.append(i)
#     for i in range (0,len(ls)):
#         for j in range (0,len(ls)):
#             if ord(ls[j])>ord(ls[i]):
#                 temp=ls[i]
#                 ls[i]=ls[j]
#                 ls[j]=temp
#     ans="".join(ls)
#     print(ans)
#     return
# sort_string(string)
# **************************************

# string="prepbytes"
# def ct_uniq_char(string):
#     visited=[]
#     count=0
#     for i in string:
#         if i not in visited:
#             count+=1
#             visited.append(i)
#     print(count)
#     return
# ct_uniq_char(string)
# **************************************

# mat1=[[1,1],
#       [2,2]]
# mat2=[[1,1],
#       [2,2]]
# res=[[0, 0],
#      [0, 0]]
# def mult_matrix(mat1,mat2,r1,c1,r2,c2):
#     for i in range (r1):
#         for j in range (c2):
#             for k in range (r2):
#                 res[i][j]+=mat1[i][k]*mat2[k][j]

#     print("Multiplication of given two matrices is: ")
#     for i in range(0, r1):
#         for j in range(0, c2):
#             print(res[i][j], end=" ")
#         print("\n", end="")
#     return
# mult_matrix(mat1,mat2,2,2,2,2)
# **************************************

# import numpy as np
# string='prepbytes'
# def permut(string):
#     ls=[]
#     for i in string:
#         ls.append(i)
#     #Any character replace with any other character within the string, so performing it randomly
#     random1=np.random.randint(0,len(string))
#     random2=np.random.randint(0,len(string))
#     temp=ls[random1]
#     ls[random1]=ls[random2]
#     ls[random2]=temp
#     ans="".join(ls)
#     print(ans)
#     return
# permut(string)
# **************************************

# P=5
# B=12
# H=13
# def area_incircle(P,B,H):
#     r=(P+B+H)/2
#     area=3.14*pow(r,2)
#     print(area)
#     return
# area_incircle(P,B,H)
# **************************************

# string="welcome to prepbytes"
# def panagrams(string):
#     string.strip(" ")
#     string.lower()
#     ans=""
#     alphabet="abcdefghijklmnopqrstuvwxyz"
#     for i in alphabet:
#         if i not in string:
#             ans+=i
#     print(ans)
#     return
# panagrams(string)
# **************************************

# temp=0
# def temp_F_to_C(temp):
#     celc=(5/9*temp)+32
#     print(celc)
#     return
# temp_F_to_C(temp)
# **************************************

# N=10
# import math
# def prime_sum(N):
#     ls=[2]
#     for i in range(3, N):
#         is_prime=True
#         sqrt_i=math.isqrt(i)  # Calculate square root of i
#         for j in range(2,sqrt_i+1):  # Check divisibility by primes up to sqrt(i)
#             if i%j==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             ls.append(i)
#     print(sum(ls))
#     return
# prime_sum(N)
# **************************************

# ls=["54","546","548","60"]
# def largest_num_create(ls):
#     ls.sort(reverse=True)
#     ans="".join(ls)
#     print(ans)
#     return
# largest_num_create(ls)
# **************************************

# E=10 #Energy the indvidual has
# exercises=[2,1] #Energy consumption of each exercise (each can be done at most 2 times, in the given order only)
# def tiredness_calc(E,exercises):
#     ct=0 # count how many time an exercise is done (max possible value is 2)
#     num_exer=0 #No. of exercises done
#     for i in range (len(exercises)):
#         E-=exercises[i]
#         ct+=1
#         num_exer+=1
#         if E>0:
#             E-=exercises[i]
#             num_exer+=1
#             ct=0
#             i+=1
#         if E<=0:
#             print(num_exer)
#             return
#     if E>0:
#         print(-1)
#         return
# tiredness_calc(E,exercises)
# **************************************

# num_heros = 1
# num_villains = 5
# health_heros = 4
# health_villains = [1, 2, 3, 1, 3,]
# count=0
# def fights(num_heros, num_villains, health_heros, health_villains):
#     global count
#     for i in range (max(num_heros,num_villains)):
#         health_sum_hero=num_heros*health_heros
#         health_sum_villain=sum(health_villains)
#         if health_sum_hero>=health_sum_villain:
#             print(count)
#             return
#         else:
#             health_villains.pop(0)
#             count+=1
#             num_villains-=1
#             fights(num_heros, num_villains, health_heros, health_villains)
#             break
            
# fights(num_heros, num_villains, health_heros, health_villains)
# **************************************

# s="leEeetcode"
# # Bad pair is when a letter (lowercase) and its uppercase are adjacent:: remove both lower and uppercased charcters
# def removeBadpairs(s):
#     stack=[]
#     for i in s:
#         if stack and abs(ord(i)-ord(stack[-1]))==32:
#             stack.pop()
#         else:
#             stack.append(i)
#     print(s)
#     return
# removeBadpairs(s)
# **************************************

# n=10 #No. of terms in fibonacci
# ls=[0,1]
# def fibonacci(n):
#     if n<=0:
#         return 
#     for i in range (n-2):
#         next_ele=ls[-1]+ls[-2]
#         ls.append(next_ele)
#     print(ls)
#     print("Sum of n terms of the fibonacci series: ", sum(ls))
#     return
# fibonacci(n)
# **************************************

# s1="abcedxyz"
# s2="ertdxyz"
# def longest_common_substring(s1,s2):
#     length=0
#     for i in range(0,len(s1)):
#         curr=s1[i]
#         for j in range(i+1,len(s1)):
#             curr=curr+s1[j]
#             if curr in s2:
#                 length=max(length,len(curr))
#     print(length)
#     return
# longest_common_substring(s1,s2)
# **************************************

# s="babad"
# def longestPalindrome(s):
#     if len(s)<=1:
#         return s
# # Moving from Centre on both sides
#     def centre_expansion(left,right):
#         while left>=0 and right<len(s) and s[left]==s[right]:
#             left-=1
#             right+=1
#         return s[left+1:right]
    
#     long_substring=s[0]
    
#     for i in range(len(s) - 1):
#         odd=centre_expansion(i,i)
#         even=centre_expansion(i,i+1)

#         if len(odd)>len(long_substring):
#             long_substring=odd
#         if len(even)>len(long_substring):
#             long_substring=even
#     print(long_substring)
#     return
# longestPalindrome(s)
# **************************************

# n=5
# ans=[]
# def num_bin(n):
#     quo=n//2
#     rem=n%2
#     ans.insert(0,rem)
#     if quo==0:
#         return ans.count(1)
#     else:
#         return num_bin(quo)
# **************************************

# num_monsters=3
# exp_points=100
# power_monster=[101,100,304]
# bonus_defeat=[100,1,524]
# def defeat_monster(num_monsters, exp_points,power_monster,bonus_defeat):
#     count=0 # maintains the count of no. of monsters defeated
#     power_monster.sort()
#     for i in range (num_monsters):
#         if exp_points>=power_monster[i]:
#             exp_points+=bonus_defeat[i]
#             count+=1
#         else:
#             break
#     print(count)
#     return
# defeat_monster(num_monsters, exp_points,power_monster,bonus_defeat)
# **************************************