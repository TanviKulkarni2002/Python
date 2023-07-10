nums=[1,3,5,6]
target=9
if target in nums:
    print(nums.index(target))
else:
    nums.append(target)
    nums.sort()
    print(nums.index(target))