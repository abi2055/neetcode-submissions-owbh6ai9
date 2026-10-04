class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        # you can either add a closing or opening parantheses
        # so for what condition do you fail and not go further 
        # rule: close < open on each iteration, ignore if that case is not true

        def dfs(openNo, closedNo, combination):
            if closedNo == openNo and openNo == n:
                results.append(combination)
                return 

            if openNo < n:
                combination += "("
                dfs(openNo + 1, closedNo, combination)
                combination = combination[:-1]
                # basically popping if its a stack
            
            if closedNo < openNo:
                combination += ")"
                dfs(openNo, closedNo + 1, combination)
                combination = combination[:-1]

        dfs(0,0, "")
        return results

            