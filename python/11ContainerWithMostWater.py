#def revisit this...
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height)-1
        areas=set()
        while(ptr2>ptr1):
            areas.add((ptr2-ptr1)*min(height[ptr1], height[ptr2]))
            if height[ptr1]<height[ptr2]: ptr1+=1
            else: ptr2-=1
        return max(areas)
        