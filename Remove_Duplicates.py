nums=[0,0,1,1,1,2,2,3,3,4]
non_dup=[]
for i in nums:
    if i not in non_dup:
        non_dup.append(i)
    else:
        continue
for i in non_dup:
    nums[i]=non_dup[i]
print(nums)
print(len(non_dup))
print(non_dup)