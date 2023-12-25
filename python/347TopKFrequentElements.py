#horrifying implementation but the algo/idea is right so...
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies={}
        flipped={}
        rv = list()
        for i in nums:
            if i not in frequencies: frequencies[i]=0
            frequencies[i]+=1
        for i in frequencies:
            if frequencies[i] not in flipped: flipped[frequencies[i]] = list()
            flipped[frequencies[i]].append(i)
        while k>0:
            a = max(flipped)
            for i in flipped[a]: rv.append(i)
            k -= len(flipped[a])
            del flipped[a]
        return rv
        