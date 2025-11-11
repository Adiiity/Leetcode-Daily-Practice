class Solution:
    def calculate(self, s: str) -> int:
        # example 1+(2-(3+4))
        sign=1
        res=0
        num=0
        stack=[]
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif ch in '+-':
                res+=sign*num
                num=0
                sign=1 if ch=='+' else -1
            elif ch==')':
                res+=sign*num
                num=0
                res*=stack.pop()
                res+=stack.pop()
        
        res+=num*sign
        return res


        