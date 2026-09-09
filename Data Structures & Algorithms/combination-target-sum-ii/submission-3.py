class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []

        def dfs(i, total):
            if total == target:
                result.append(combination.copy())
                return
            if total > target or i == len(candidates):
                return 

            combination.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            combination.pop()

            # use another index for repeats, cause this is essentially the same sub tree
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, total)
    
        dfs(0, 0)

        return result