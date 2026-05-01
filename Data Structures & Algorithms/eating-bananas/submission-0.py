class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Calculate each potentially eating rate in a for loop
        
        largest_k = 0
        for i in range(len(piles)):
            largest_k = max(largest_k, piles[i])
        
        smallest_k = 1
        result = 0

        while smallest_k <= largest_k:
            mid = (smallest_k + largest_k) // 2
            sum_of_hours = 0
            for i in range(len(piles)):
                sum_of_hours = sum_of_hours + math.ceil(piles[i]/mid)
            if sum_of_hours > h:
                smallest_k = mid + 1
            else:
                result = mid
                largest_k = mid - 1

        return result


