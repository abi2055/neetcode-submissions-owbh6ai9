class Solution:
    def isValid(self, s: str) -> bool:

        # A strategy where the closing and opening parantheses are next to eachother
        
        stack = []
        bracket_list = {')': '(', '}': '{', ']': '['}

        for ch in s: 
            if ch in bracket_list:
                if stack and stack[-1] == bracket_list.get(ch):
                # without popping, verify non-empty stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        if stack:
            return False
        else:
            return True