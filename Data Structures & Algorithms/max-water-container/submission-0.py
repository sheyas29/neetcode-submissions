class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        while i<j:
            if heights[i]<heights[j]:
               area=heights[i]*(j-i)
               max_area=max(max_area,area)
               i+=1
            elif heights[i]>=heights[j]:
               area=heights[j]*(j-i)
               max_area=max(max_area,area)
               j-=1
        return max_area