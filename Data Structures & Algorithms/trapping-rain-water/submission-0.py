class Solution:
    def trap(self, height: List[int]) -> int:
        
        # min(L, R) - height if position i

        max_left = 0
        max_right = 0
        max_left_store = []
        max_right_store = []
        water_pos_i = 0
        res = 0
        
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[len(height) - 1 - i])
            max_left_store.append(max_left)
            max_right_store.append(max_right)

        max_right_store.reverse()

        for i in range(len(height)):
            water_pos_i = min(max_left_store[i], max_right_store[i]) - height[i]
            if water_pos_i > 0:
                res += water_pos_i
            
        return res