class Solution:
    def myAtoi(self, s: str) -> int:
        # avoid white spaces 
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        if i==n:
            return 0

        # sign check
        sign=1
        if s[i]=='-' or s[i]=='+':
            sign=-1 if s[i]=='-' else 1
            i+=1
        #rounding check 
        INT_MAX=2**31-1
        INT_MIN=-2**31

        res=0
        while i<n and s[i].isdigit():
            # convert str to int 
            digit=ord(s[i])-ord('0')

            if res>INT_MAX//10 or (res==INT_MAX//10 and digit>INT_MAX%10):
                return INT_MAX if sign==1 else INT_MIN
            res=res*10+digit
            i+=1
        
        return sign*res
