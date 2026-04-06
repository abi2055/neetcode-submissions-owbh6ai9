class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # take the middle length of the array nums
        # if that middle value is larger than the target remove the right half of nums
        # if the middle value is smaller than the target remove the left half of the nums
        # if the middle value is the target return the middle value

        pointer_right = len(nums) - 1
        pointer_left = 0

        while pointer_left <= pointer_right:
            mid = (pointer_left + pointer_right) // 2
            if nums[mid] > target:
                pointer_right = mid - 1
            elif nums[mid] < target:
                pointer_left = mid + 1
            else:
                return mid

        return -1

        

