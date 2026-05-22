class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # formula aka time = (target - position) / speed

        # list comprehension
        combined = [[pos, speed] for pos, speed in zip(position, speed)]

        # sorting for traversal purposes
        combined = sorted(combined)

        stack = []

        for pos, speed in combined[::-1]:
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)


        