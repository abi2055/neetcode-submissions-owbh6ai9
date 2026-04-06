class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if largest == second:
                heapq.heappush_max(stones, 0)
            else:
                heapq.heappush_max(stones, largest - second)

        return stones[0]
