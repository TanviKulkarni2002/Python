'''Consider the following Python Program. It reads integers from the standard input (until it gets a negative number) and puts them 
into an array. After that it calls processArray on the array, and then prints the contents of the array on standard output.
Currently, processArray does not modify the array. You have to change this program so that any sequence of two or more consecutive 
numbers greater than or equal to 100 in the array are removed from the array and replaced with just the first number of the sequence. 
In other words, in any sequence of numbers greater than or equal to 100, only the first number is retained and the others are removed. 
The processArray method should modify the array in-place (preferably without creating a new array), and it should return the new 
length of the modified array.'''

#Solution:

li = [3,116,136,61,11,616,216,376,61,6,-1]
arr = []
for i in li:
    if(i>0):
        arr.append(i)
    else:
        break

for x in range (0,len(arr)):
    for j in range (0,len(arr)+1):
        if(j+1<len(arr)):
            if(arr[j]>=100 and arr[j+1]>=100):
                del arr[j+1]

print(arr)