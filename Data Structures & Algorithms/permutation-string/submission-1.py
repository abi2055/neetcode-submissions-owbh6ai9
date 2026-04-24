class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # put everything s1 in a hashmap
        # put the sliding window of s2 in a hashmap and compare

        s1_count = {}
        s2_count = {} 

        p1 = 0
        p2 = len(s1)

        window = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

        if s1_count == s2_count:
            return True

        window = len(s1)

        for p2 in range(window, len(s2)):
            s2_count[s2[p2]] = s2_count.get(s2[p2], 0) + 1
            s2_count[s2[p1]] = s2_count.get(s2[p1], 0) - 1


            if s2_count[s2[p1]] == 0:
                del s2_count[s2[p1]]

            p1 += 1 

            if s1_count == s2_count:
                return True

        return False

            


                



