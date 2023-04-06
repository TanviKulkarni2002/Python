num = str(input("Enter the number: "))
li = []
li_rev = []
for i in num:
    li.append(i)

if(li[0]=='-'):
    li.reverse()
    del li[-1]
    li.insert(0,'-')
else:
    li.reverse()
str_rev = ''.join(li)
print("Reversed Integer is: ",str_rev)