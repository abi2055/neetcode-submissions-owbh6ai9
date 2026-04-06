class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix calculation and mapping
        # create 2 arrays prefix and suffix 
        # for each number ignore the current value, take whatever comes before and whatever comes after 
        # and multiply them 

        prefix = [1] * len(nums)
        # 1 since, 1 x anything is = anything
        suffix = [1] * len(nums)
        result = [1] * len(nums)
 
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        print(prefix)

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        print(suffix)

        for i in range(len(nums)):
            result[i] = prefix[i]*suffix[i]
        
        print(result)

        return result
