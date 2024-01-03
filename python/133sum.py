class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rv = list()
        nums.sort()
        if len(nums) < 3: return []
        for i, n in enumerate(nums):
            if i!=0 and nums[i-1] == n: continue
            if i == len(nums)-1: break
            ptr1 = i+1
            ptr2 = len(nums)-1
            while ptr1<ptr2:
                if nums[ptr1] + nums[ptr2] == -n:
                    rv.append([n, nums[ptr1], nums[ptr2]])
                    temp = nums[ptr2]
                    while ptr2 >= 0 and temp == nums[ptr2]: ptr2-=1
                    temp = nums[ptr1]
                    while ptr1 < len(nums) and temp == nums[ptr1]: ptr1+=1
                elif nums[ptr1] + nums[ptr2] > -n:
                    temp = nums[ptr2]
                    while ptr2 >= 0 and temp == nums[ptr2]: ptr2-=1
                else: 
                    temp = nums[ptr1]
                    while ptr1 < len(nums) and temp == nums[ptr1]: ptr1+=1
        return rv
