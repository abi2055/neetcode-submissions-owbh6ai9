class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a frequency count dict/hashmap
        # depening on k, get the largest counts in the dict

        frequency_count = {}
        top_nums = []

        for num in nums:
            if num in frequency_count:
                frequency_count[num] += 1
            else:
                frequency_count[num] = 1
        
        for i in range(k):
            max_key = max(frequency_count, key=frequency_count.get)
            top_nums.append(max_key)
            del frequency_count[max_key]

        return top_nums

