nums=[1,2,3,4]
ls=[]
for i in range (0,len(nums)):
    ans=sum(nums[0:i+1])
    ls.append(ans)
print(ls)