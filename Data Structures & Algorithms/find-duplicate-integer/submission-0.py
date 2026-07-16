class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast slow pointer approach
        # when the fast pointer loops back 

        # floys algorithm

        slow_pointer = 0
        fast_pointer = 0
        while True:
            slow_pointer = nums[slow_pointer]
            # advancing one edge/link
            fast_pointer = nums[nums[fast_pointer]]
            # advancing two edges/links
            if slow_pointer == fast_pointer:
                break

        p = 0
        while True:
            slow_pointer = nums[slow_pointer]
            p = nums[p]
            if slow_pointer == p:
                return slow_pointer