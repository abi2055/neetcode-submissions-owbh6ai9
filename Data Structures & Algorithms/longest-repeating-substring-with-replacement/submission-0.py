class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_count = {}
        window = 0
        largest_window = 0

        p1 = 0
        # p2 = 0

        most_frequent = 0

        # attempt 1
        # for i in range(len(s)):
        #     for value in frequency_count.values():
        #         most_frequent = max(value, most_frequent)
            
        #     if window - most_frequent <= k:
        #         frequency_count[s[p2]] = frequency_count.get(s[p2], 0) + 1
        #         p2 += 1 
        #     else:
        #         frequency_count[s[p1]] = frequency_count.get(s[p1], 0) - 1
        #         p1 += 1

        #     window = p2 - p1

        #     largest_window = max(window, largest_window)

        # return largest_window

        for p2 in range(len(s)):
            frequency_count[s[p2]] = frequency_count.get(s[p2], 0) + 1
            most_frequent = max(most_frequent, frequency_count.get(s[p2]))

            window = p2 - p1 + 1

            while window - most_frequent > k:
                frequency_count[s[p1]] -= 1
                p1 += 1
                window = p2 - p1 + 1
            
            largest_window = max(window, largest_window)
            
        return largest_window


