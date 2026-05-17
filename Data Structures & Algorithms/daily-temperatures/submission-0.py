class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep temperatures in stack
        # we pop until element has bigger than amount
        # we dont care if they are lost during the pop
        results = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                # top of the stack is -1 to peek
                stack_index, stack_temp = stack.pop()
                results[stack_index] = index - stack_index
                # i - stack_index basically gives us the number of days in the future

            stack.append([index, temp])

        return results




