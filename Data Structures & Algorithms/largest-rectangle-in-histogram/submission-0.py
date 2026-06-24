class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_result = 0
        stack = []

        for i, h in enumerate(heights):
            start_index = i
            while stack and stack[-1][1] > h:
                # the top of the stack's height is greater than current height
                index, height = stack.pop()
                largest_result = max(largest_result, (i - index) * height)
                # the smallest height would be limiting
                start_index = index
            stack.append((start_index, h))

        for i, h in stack:
            largest_result = max(largest_result, (len(heights) - i) * h)

        return largest_result

