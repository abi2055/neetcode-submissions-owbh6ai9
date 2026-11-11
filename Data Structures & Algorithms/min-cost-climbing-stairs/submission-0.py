class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # basically a decision tree with memoization to reduce time complexity
        # the top down solution invoved dfs with memo and a base case 
        # the bottom up seems more intuitive where every cell contains the amount it takes to get to the end
        # and it build up

        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[len(cost)]
