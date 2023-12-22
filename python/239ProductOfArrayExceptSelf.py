#actually so trivial
#they did hint at it though
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rv = list()

        pre = 1
        for n in nums:
            rv.append(pre)
            pre *= n

        suf = 1
        for i in range(len(nums))[::-1]:
            rv[i]*=suf
            suf*= nums[i]
        return rv
            