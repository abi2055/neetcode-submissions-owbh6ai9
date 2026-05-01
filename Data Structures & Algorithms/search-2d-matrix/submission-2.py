class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the appropriate row
        # do binary search on that appropriate row 

        rows = len(matrix)
        cols = len(matrix[0])
        
        top_row = 0
        bottom_row = rows - 1

        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
            if target > matrix[mid_row][cols-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
            else:
                break
            
        if top_row > bottom_row:
            return False

        mid_row = (top_row + bottom_row) // 2
        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[mid_row][mid]:
                left = mid + 1
            elif target < matrix[mid_row][mid]:
                right = mid - 1
            else:
                return True
            
        return False


        
