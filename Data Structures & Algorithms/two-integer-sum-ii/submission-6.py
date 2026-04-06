class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # kind of looking at all combinations so it would be 2^n-1 2^3=8 
        # my idea is to go through each element, but once its been checked
        # never check that index again
        # if a combination is ever larger than the target
        # then you immediately skip any more combinations with that index 
        # and go to the next

        first = 0
        second = first + 1 # 1 = i

        # for i in range(len(numbers)):
        #     if (numbers[first] + numbers[second]) < target:
        #         second = first + 1
        #     elif (numbers[first] + numbers[second]) == target:
        #         return [numbers[first], numbers[second]]
        #     else (numbers[first] + numbers[second]) > target:
        #         first += 1

        while (numbers[first] + numbers[second]) != target:
            if (numbers[first] + numbers[second]) == target:
                return [first+2, second+2]
            elif second != len(numbers)-1: 
                second += 1
            else:
                first += 1
                second = first + 1
            print("first: ", first)
            print("Second: ", second)

        return [first+1, second+1]



        # [1,2,3] target 5
        # 1: 1+2 = 3, second should move to 3, index 2, second = 1
        # 2: 1+3 = 4, second = 2, second will reset to first + 1
        # 3: 2+3 = 5, first = 1, second = 2




