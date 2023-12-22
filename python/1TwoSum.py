# Brute Force Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rv = [0,0]
        n = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    rv[0]=i
                    rv[1]=j
                    return rv
        