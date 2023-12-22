#first sol I thought of
#O(n) time, O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        for i in nums:
            if i in appeared:
                return True
            appeared[i] = 0

#sol but with set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
        for i in nums:
            if i in appeared:
                return True
            appeared.add(i)
        return False