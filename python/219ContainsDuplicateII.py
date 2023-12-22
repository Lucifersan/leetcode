#2nd attempt after first failed due to time complexity
#O(n) time, O(n) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        index = 0
        for i in nums:
            if i in indices and abs(indices[i]-index)<=k:
                return True
            indices[i]=index
            index += 1
        return False
        