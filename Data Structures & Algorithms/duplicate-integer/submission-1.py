class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create a dictionary that counts frequency
        # check if the frequency is greater than 1
        # break when the first one is found true

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        