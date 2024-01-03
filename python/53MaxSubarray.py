#this code is cancer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rv = 0
        prefixsum = [0 for i in nums]
        for i, n in enumerate(nums):
            if i == 0:
                prefixsum[i] = n
            else:
                prefixsum[i] = prefixsum[i-1]+n
        currmax = 0
        adj = 0
        allneg = True
        for i, n in enumerate(prefixsum):
            currmax += nums[i]
            if n-adj < 0:
                currmax = 0
                adj = n
            if currmax > rv:
                rv = currmax
            if nums[i] > 0: allneg = False
        if allneg: return max(nums)
        return rv