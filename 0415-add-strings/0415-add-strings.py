class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i,j=len(num1)-1,len(num2)-1
        carry=0
        s=0
        res=[]
        while i>=0 or j>=0 or carry:
            digit1=(ord(num1[i])-ord('0')) if i>=0 else 0
            digit2=(ord(num2[j])-ord('0')) if j>=0 else 0

            s=digit1+digit2+carry
            res.append(str(s%10))
            carry=s//10

            i-=1
            j-=1

        return "".join(reversed(res))
        