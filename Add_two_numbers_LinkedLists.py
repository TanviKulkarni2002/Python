#l1,l2 are Singly Linked Lists
resHead=ListNode(0)
tail=resHead #Pointer
carry=0

while (l1 is not None) or (l2 is not None) or carry!=0:
    if(l1 is not None):
        digit1=l1.val
    else:
        digit1=0
            
    if(l2 is not None):
                digit2=l2.val
    else:
        digit2=0
            
    sum=digit1+digit2+carry
    new_digit=sum%10
    carry=sum//10

    newNode=ListNode(new_digit)
    tail.next=newNode
    tail=tail.next

    if(l1 is not None):
        l1=l1.next
    else:
        l1=None
            
    if(l2 is not None):
        l2=l2.next
    else:
        l2=None
        
ans=resHead.next
resHead.next=None
print(ans)