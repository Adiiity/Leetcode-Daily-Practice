class Solution:
    def isValid(self, s: str) -> bool:
        valid_map={")":"(","}":"{","]":"["}
        stack=[]

        for c in s:
            if c in valid_map:
                if stack and stack[-1]==valid_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
