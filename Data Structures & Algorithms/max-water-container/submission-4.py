class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # if i have two pointers starting at the start
        # that will be the max index 1 and index 2
        # you move the rght pointer across to check the next if its smaller
        # dont update the max
        # then you move the left pointer across
        # if thats larger you updates the largest 
        
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
            print("L: ", l)
            print("R: ", r)
        
        return largest