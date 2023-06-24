nums=[0,1,2,2,3,0,4,2]
val=2
nums.sort()
for i in nums:
    if i==val:
        nums.remove(i)
        nums.append(i)
    else:
        continue
count=0
for i in range(0,len(nums)):
    if nums[i]!=val:
        count+=1
    else:
        print(count)
        break