class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rv = 0
        temp = 0
        seen = set()
        i=0
        indices={}
        while i < len(s):
            if s[i] not in seen: 
                temp += 1
                seen.add(s[i])
                indices[s[i]]=i
                i+=1
            else: 
                rv = max(temp, rv)
                i=indices[s[i]]
                indices = {}
                seen = set()
                temp = 0
                i+=1
        return max(temp,rv)