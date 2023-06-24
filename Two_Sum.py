nums=[2,7,11,15]
target=9
for ind1 in range (0,len(nums)):
    for ind2 in range(ind1+1,len(nums)):
        if(nums[ind1]==target-nums[ind2]):
            print(ind1,ind2)