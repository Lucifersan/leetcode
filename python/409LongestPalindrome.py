class Solution:
    def longestPalindrome(self, s: str) -> int:
        rv = 0
        n=len(s)
        odd = False
        if n==0: return rv
        d = Counter(s)
        for i in d.values():
            rv += (i//2)*2
            if i%2 == 1: odd = True
        if odd: rv +=1
        return rv
        