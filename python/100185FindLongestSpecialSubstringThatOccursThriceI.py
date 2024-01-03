#one of the worst pieces of code ive written to dete but it certainly works...
class Solution:
    def maximumLength(self, s: str) -> int:
        counter = {}
        curr = s[0]
        temp = ""
        for i in s:
            if curr != i:
                for j in range(1, len(temp) + 1):
                    if temp[0:j] not in counter: counter[temp[0:j]] = 0
                    counter[temp[0:j]] += len(temp) - j + 1
                temp = ""
                curr = i
            temp+=i
            
        #stupid fix but just do it again if it never hits a curr!=i point
        for j in range(1, len(temp) + 1):
            if temp[0:j] not in counter: counter[temp[0:j]] = 0
            counter[temp[0:j]] += len(temp) - j + 1
        
        rv = -1
        for i in counter:
            if counter[i] >= 3:
                if len(i) > rv: rv = len(i)
            #this is presumably unnecessary now but I'm too scared to take it out
            if len(i)-2 > rv and len(i)-2 > 0:
                rv = len(i)-2      
        return rv
        
        
        