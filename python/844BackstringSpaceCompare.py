class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = list()
        stack2 = list()
        for i in s:
            if i == "#" and len(stack1)==0: pass
            elif i == "#": stack1.pop()
            else: stack1.append(i)
        for i in t:
            if i == "#" and len(stack2)==0: pass
            elif i == "#": stack2.pop()
            else: stack2.append(i)
        return stack1==stack2
        