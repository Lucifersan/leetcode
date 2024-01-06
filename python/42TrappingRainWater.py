class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = list()
        maxright = list()
        minrl = list()

        temp = 0
        for i in height:
            maxleft.append(temp)
            temp = max(temp,i)
        temp = 0
        for i in height[::-1]:
            maxright.append(temp)
            temp = max(temp,i)
        maxright = maxright[::-1]
        for i in range(len(height)):
            minrl.append(min(maxleft[i], maxright[i]))
        
        rv = 0
        for i in range(len(height)):
            if minrl[i]-height[i] > 0: rv += minrl[i]-height[i]

        return rv