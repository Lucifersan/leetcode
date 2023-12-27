#cannot believe brute force was the way to go
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        rv = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = math.gcd(temp,nums[j])
                if temp == k:
                    rv += 1
                elif temp < k:
                    break
        return rv

        