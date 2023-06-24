def scramble(s1, s2):
    pass # your code here
    li1=[]
    li2=[]
    ans=False
    for i in s1:
        li1.append(i.lower())
    for i in s2:
        li2.append(i.lower())
        
    for i in li2:
        if i in li1:
            li1.remove(i)
            ans=True
        else:
            ans=False
            break
    print(ans)
scramble("TanVi","")