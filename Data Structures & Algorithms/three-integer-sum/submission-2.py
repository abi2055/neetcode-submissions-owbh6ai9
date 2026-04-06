class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # you go through each element once
        # and you essentially just twosum the remaining ones 
        # sort them first
        
        res_list = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue 
            # if you encounter a duplicate thats not the first value in the array
            # skip since we already looked at that permutation basically

            left = 1 + index
            right = len(nums)-1

            while left < right:
                if value + nums[left] + nums[right] > 0:
                    right -= 1
                elif value + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res_list.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return res_list

        

