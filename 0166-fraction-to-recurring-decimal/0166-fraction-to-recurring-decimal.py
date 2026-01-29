class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        # Handle zero numerator
        if numerator==0:
            return '0'
        
        # Handle zero denominator
        if denominator==0:
            return 'Undefined'

        res=[]
        # Handle sign 
        if (numerator<0) ^ (denominator<0):
            res.append("-")
        
        # only positive values
        n=abs(numerator)
        d=abs(denominator)

        # Integer part
        quo_int=n//d
        res.append(str(quo_int))

        # if remainder is 0
        rem=n%d
        if rem==0:
            return "".join(res)
        
        #  add decimal
        res.append(".")

        # decimal part
        seen={}
        while rem!=0:
            if rem in seen:
                pos=seen[rem]
                res.insert(pos,"(")
                res.append(")")
                break
            # record position
            seen[rem]=len(res)

            rem*=10
            quo=rem//d
            res.append(str(quo))
            rem%=d

        return "".join(res)
        




        