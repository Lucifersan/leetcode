#i feel really stupid coz
#everyone had the same sol
#and i popped
#apparently depending on the kind of python
#this might be O(N^2) bc pop
#oh well
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            temp = nums.pop(0)
            if temp != val:
                nums.append(temp)
        return len(nums)
            