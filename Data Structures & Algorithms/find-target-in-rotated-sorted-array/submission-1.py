class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left half sorted
            if nums[l] <= nums[mid]:
                # this is the range of values in the left portion
                # if the target is inside we keep the left side
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # discard left
                else:
                    l = mid + 1
            # right half sorted
            else:
                # this is the range of values in the right portion
                # if the target is inside the range we keep the right side
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
