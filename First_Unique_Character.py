def firstUniqChar():
    temp=[]
    ans=-1
    s='abcdeafb'
    for i in s:
        temp.append(i)
    for j in temp:
        x=temp.count(j)
        if(x>1):
            x=0
            ans=-1
        if(x==1):
            ans=temp.index(j)
            break
    print(ans)
firstUniqChar()