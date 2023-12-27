#easy but i wrote it cursed for fun
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            n = ord(i)-ord("a")
            if n >= 0 and n<26:
                new += i
            n = ord(i)-ord("A")
            if n >= 0 and n < 26:
                new += chr(n+ord("a"))
            n = ord(i)-ord("0")
            if n >= 0 and n < 10:
                new += chr(n+ord("0"))
        for i in range(len(new)//2):
            if new[i] != new[-(i+1)]: return False
        return True