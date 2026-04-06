class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # so the sliding window idea i have in mind 
        # is to first find the window of the largest non repeating substring
        # this will update each time a new one is found and that will be the window
        # as the window moves through the string, the window will try to increase by 1
        # we will take the set of the increased string 
        # if the set is equal to the original string that means the larger substring has a duplicate

        # window = 1
        # longest = 0
        # first_pointer = 0

        # while first_pointer != len(s):
        #     substr = s[first_pointer:window+first_pointer]
        #     print("substring: ", substr)
        #     print("set substring: ", set(substr))
        #     if substr != set(substr):
        #         longest = len(set(substr))
        #         # print(longest)
        #         first_pointer += 1
        #         # this would be a duplicate, window stays the same
        #         # update to next element automatically, keep longest the length of the substring 
        #     else:
        #         # non-duplicate
        #         # window should increase by 1
        #         window += 1

        # return longest

        seen = set()
        left = 0
        best = 0

        for right, ch in enumerate(s):
            # shrink window until no duplicate of ch
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            best = max(best, right - left + 1)

        return best