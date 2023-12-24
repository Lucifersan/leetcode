class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        lengths = list()
        for i in nums:
            if i - 1 in numset: continue
            temp = 1
            n=1
            while i+n in numset:
                temp += 1
                n+=1
            lengths.append(temp)
        return max(lengths)