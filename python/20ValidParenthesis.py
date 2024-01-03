class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        matched = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i in matched.values():
                stack.append(i)
            if i in matched:
                if len(stack)==0 or matched[i] != stack.pop():
                    return False
        if len(stack)!=0: return False
        return True           
        