class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force is pretty simple
        # use the window size to slide across 
        # calculate the max of that sub window at each point
        # not really optimal however 

        # using a heap data structure to remove and lookup quickly 
        # might be more efficient 

        # the other could be to save the largest value in each list 

        # constantly push to the heap but check 
        # if the max elements remains in the structure 

        # 1. brute force 

        lp = 0
        rp = k
        res = []

        for i in range(0, len(nums)-k+1):
            largest = float("-inf")
            for c in range (lp, rp):
                if nums[c] > largest:
                    largest = max(largest, nums[c])

            print("left pointer: ", lp)
            print("right pointer: ", rp)
            
            res.append(largest)
            lp += 1
            rp += 1
            
        return res