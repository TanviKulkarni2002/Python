def return_duplicates():
    val = False
    li = [1,2,3,4,1]
    li.sort()
    for i in range (0,len(li)):
        if(li[i-1]==li[i]):
            val = True
    print(val)
return_duplicates()

#Alternative Way:
nums = [1,2,3,1]
rem_dup = set(nums)
if (len(rem_dup)<len(nums)):
    print("True")
if (len(rem_dup)==len(nums)):
    print("False")