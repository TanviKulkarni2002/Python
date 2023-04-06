class Solution:
    def isMatch(s: str, p: str):
        res=False
        a=''
        p1=p.lstrip(a)
        #print(p1)

        while True:
            if(p1=='*'):
                p=p.rstrip('*')
                if(len(s)>=len(p)):
                    res=True
                    break
                else:
                    res=False
                return res
        
            elif(p1=='.'):
                p=p.rstrip('.')
                if(len(s)==len(p)):
                    res=True
                    break
                else:
                    res=False
                return res
        
            elif(p1=='*.'):
                p=p.rstrip('*.')
                if(len(s)>=len(p) or len(s)==len(p)):
                    res=True
                    break
                else:
                    res=False
                return res
    isMatch('aaa','a*')