#today i learned syntax
class Solution:
    def countAnagrams(self, s: str) -> int:
        rv = 1
        mod = 10**9 + 7
        for word in s.split(" "):
            letters, temp = Counter(word), factorial(len(word))
            for val in letters.values():
                temp = temp // factorial(val)
            rv *= temp%mod
        return rv%mod