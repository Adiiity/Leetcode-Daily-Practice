class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i,write=0,0
        n=len(chars)
        while i<n:
            j=i
            currChar=chars[i]
            while j<n and chars[j]==currChar:
                j+=1

            count=j-i
            chars[write]=currChar
            write+=1
            if count>1:
                for s in str(count):
                    chars[write]=s
                    write+=1
            i=j
        return write



