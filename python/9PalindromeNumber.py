#mistake made: if s[i]!=s[-i] is wrong since 
#index starts at 0, for -1
#to match with 0 you need to -(i+1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        length = len(s)
        for i in range(length):
            if s[i]!=s[-(i+1)]:
                return False
        return True
