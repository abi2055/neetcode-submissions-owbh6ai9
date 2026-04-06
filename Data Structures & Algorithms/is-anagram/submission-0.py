class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # different solutions 

        # for loop that stores letters in dict 
        # o(len(s) + len(t)) -> O(n)

        # or just sort both and compare

        if sorted(s) == sorted(t):
            return True

        return False