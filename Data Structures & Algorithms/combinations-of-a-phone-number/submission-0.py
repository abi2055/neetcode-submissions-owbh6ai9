class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # per number has 3 potential characters 
        # 3 to the power of the number of digits is the number of combinations
        # start with a dictonary mapping of digit to character string

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # for example 34 
        # finds 3 gets the string, finds 4 gets the string 
        # create the combinations using dfs

        results = []

        def dfs(i, combination):
            if i >= len(digits):
                results.append(combination)
                return 

            for c in phone[digits[i]]:
                dfs(i + 1, combination + c)
                
        if digits:
            dfs(0, "")
        
        return results




