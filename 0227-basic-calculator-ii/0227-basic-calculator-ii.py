class Solution:
    def calculate(self, s: str) -> int:
        
        s=s.strip()
        if not s:
            return 0
        
        res=0
        op='+'
        num=0
        last=0

        # example 3+2*2

        for ch in s + '+':
            if ch==' ':
                continue
            if ch.isdigit():
                num=num*10+int(ch)
            else:
                if op=='+':
                    res+=last
                    last=num
                elif op=='-':
                    res+=last
                    last=-num
                elif op=='/':
                    last=int(last/num)
                elif op=='*':
                    last=last*num

                num=0
                op=ch

        return res+last                



