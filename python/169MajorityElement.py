#first thought: basically a brute force but with a dictionary!!!
#time O(n) space O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsFreq = {}
        for i in nums:
            if i in numsFreq:
                numsFreq[i]+=1
            else:
                numsFreq[i]=1
        maxValKey = nums[0]
        for i in nums:
            if numsFreq[i] > numsFreq[maxValKey]:
                maxValKey=i
        return maxValKey
        