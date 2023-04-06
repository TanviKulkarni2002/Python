prices=[2,4,1]
profit=0
temp1=prices[0]
ind1=0
for i in range (0,len(prices)): #Buy the stocks
    if prices[i]<temp1:
        temp1=prices[i]
        ind1=i

temp2=temp1
ind2=ind1
for j in range (ind1,len(prices)): #Sell the stocks
    if prices[j]>temp2:
        temp2=prices[j]
        ind2=j

ans=temp2-temp1
ans=max(profit,ans)
print(ans)