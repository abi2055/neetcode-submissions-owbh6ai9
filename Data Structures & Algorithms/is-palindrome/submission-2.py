class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(char for char in s if char.isalnum()).lower()

        first = 0
        last = len(cleaned)-1

        while first < last:
            if (cleaned[first] != cleaned[last]):
                return False
            first += 1
            last -= 1

        return True