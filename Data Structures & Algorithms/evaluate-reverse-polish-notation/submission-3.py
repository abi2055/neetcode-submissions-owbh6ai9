class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # convert tokens to a stack 
        # or push all numbers into the stack or operations into the stack first

        # push numbers and operations into independent stacks
        # and go back and fourth popping and in between add a bracket 

        stack_numbers = []
        calculation = 0 

        for token in tokens:
            if token == "/" or token == "+" or token == "-" or token == "*":
                num_a = int(stack_numbers.pop())
                num_b = int(stack_numbers.pop())
                if token == "+":
                    calculation = num_b + num_a
                elif token == "-":
                    calculation = num_b - num_a
                elif token == "*":
                    calculation = num_b * num_a
                elif token == "/":
                    calculation = num_b / num_a
                
                stack_numbers.append(calculation)

            else:
                stack_numbers.append(token)

        return int(stack_numbers.pop())