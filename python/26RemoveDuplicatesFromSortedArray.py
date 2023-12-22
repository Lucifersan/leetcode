#reading comprehension: did not have to pop...
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        while ptr1<len(nums)-1 and ptr2<len(nums):
            while ptr2<len(nums) and nums[ptr1]==nums[ptr2]:
                ptr2+=1
            for i in range(ptr1, ptr2-1):
                nums.pop(ptr1)
                ptr2-=1
            ptr1 = ptr2
            ptr2 = ptr1 + 1
        return len(nums)
    
#this is slightly  less stupid
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        k = 1
        for ptr2 in range(len(nums)):
            if nums[ptr1] != nums[ptr2]:
                ptr1 += 1
                nums[ptr1]=nums[ptr2]
                k+=1
        return k