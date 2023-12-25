#this is really stupid
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {} 
        counts[0]=0
        counts[1]=0
        counts[2]=0
        for i in nums: 
            counts[i] += 1
        for i in range(len(nums)):
            if counts[0] > 0:
                counts[0]-=1
                nums[i]=0
            elif counts[1] > 0:
                counts[1]-=1
                nums[i]=1
            else:
                counts[2]-=1
                nums[i]=2
        