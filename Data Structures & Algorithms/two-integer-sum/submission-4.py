class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i, n in enumerate(nums):
            memory[n] = i

        for i, n in enumerate(nums):
            compliment = target - nums[i]
            if compliment in memory and memory[compliment] != i:
                return [i, memory[compliment]]

# 3 + 4 target 7
# memory[3] = 1, memory[4] = 2, memory[5] = 3, memory[6] = 4
# [3,4,5,6]
# compliment = 7 - 3 = 4
# compliment is in memory
# memor
