class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        trailing = 0
        for i in nums:
            if i%2==0: trailing += 1
        if trailing >= 2: return True
        return False
        