nums=[-2,1,-3,4,-1,2,1,-5,4]
currmax=nums[0]
res=nums[0]
for i in range (1,len(nums)):
    currmax=max(currmax+nums[i],nums[i])
    res=max(res,currmax)
print(res)