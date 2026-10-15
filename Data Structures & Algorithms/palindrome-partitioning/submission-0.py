class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # you start with an empty list
        # two options a and b 
        # are those palindromes add to result 
        # palindrome logic if first half matches second half its a palindrome 
        
        results = []
        subset = []

        def dfs(i):
            if i >= len(s):
                results.append(subset.copy())
                return
            # when the subset reaches the length of the word append it to the results
            for c in range(i, len(s)):
                if checkPalindrome(i, s, c):
                    # current character, string, current loop
                    subset.append(s[i:c+1])
                    dfs(c+1)
                    subset.pop()
        
        def checkPalindrome(i, s, c):
            while i < c:
                if s[i] != s[c]:
                    return False
                i += 1
                c -= 1
            return True

        dfs(0)
        return results