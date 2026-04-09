class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If we only care about what comes before and after
        # not the actual number itself 

        converted = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in converted:
            # trying to find numbers that start the sequence
                length = 0
                while (num+length) in converted:
                    # checking if numbers can be chained in a series
                    length += 1
                longest = max(length, longest)

        return longest
                

        