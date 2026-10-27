class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        lptr = 0
        rptr = len(heights) - 1
        while lptr < rptr: 
            area = min(heights[lptr], heights[rptr]) * (rptr - lptr)
            if area > max: 
                max = area 
            if heights[lptr] < heights[rptr]: 
                lptr += 1
            else:
                rptr -= 1

        
        return max