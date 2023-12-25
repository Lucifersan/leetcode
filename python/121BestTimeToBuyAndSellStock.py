#first thought: brute force
#failed on time complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i] > maxdiff:
                    maxdiff = prices[j]-prices[i]
        return maxdiff

#tried again, succeeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        recentmin=prices[0]
        for i in range(len(prices)):
            maxprof=max(maxprof,prices[i]-recentmin)
            recentmin=min(recentmin,prices[i])
        return maxprof 
