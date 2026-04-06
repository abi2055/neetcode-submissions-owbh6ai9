class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create a dictionary that counts frequency
        # check if the frequency is greater than 1
        # break when the first one is found true

        frequency = {}
        dupe = False

        for num in nums: 
            if num not in frequency:
                frequency[num] = 1
            else:
                dupe = True

        return dupe

        