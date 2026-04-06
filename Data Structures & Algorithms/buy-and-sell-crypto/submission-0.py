class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # if you follow a two pointer approach
        # pointer one on first element
        # pointer two on the second element 
        # check if pointer one, so on buy day 1, is greater than price on day 2
        
        left = 0
        right = 1
        cur_profit = 0
        max_profit = 0

        while right < len(prices):
            # check profitablity
            if prices[left] < prices[right]:
                # we know theres a jump, so profit can be made
                cur_profit = prices[right] - prices[left]
                max_profit = max(max_profit, cur_profit)
            else:
                left = right
            right += 1
        
        return max_profit

        # current profit 1, max = 0, 
