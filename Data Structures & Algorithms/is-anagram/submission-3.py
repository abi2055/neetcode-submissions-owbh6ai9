class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # different solutions 

        # for loop that stores letters in dict 
        # o(len(s) + len(t)) -> O(n)

        # or just sort both and compare
        # if sorted(s) == sorted(t):
        #     return True

        # return False

        # Less Pythonic but still optimal

        counter_dict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counter_dict[s[i]] = counter_dict.get(s[i], 0) + 1
            counter_dict[t[i]] = counter_dict.get(t[i], 0) - 1

        for value in counter_dict.values():
            if value != 0:
                return False
        
        return True






