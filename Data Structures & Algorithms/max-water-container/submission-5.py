class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        r = len(heights)-1
        l = 0
        largest = 0
        shortest_bar = 0

        while r > l:
            shortest_bar = min(heights[r], heights[l])
            area = shortest_bar*(r-l)
            largest = max(area, largest)
            if heights[r] > heights[l]:
                l = l + 1
            elif heights[r] < heights[l]:
                r = r - 1
            else:
                r = r - 1
        
        return largest