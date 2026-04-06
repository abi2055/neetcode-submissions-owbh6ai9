class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            len_of_string = len(word)
            encoded = encoded + str(len_of_string) + "#" + word 
            # this probably needs to be modified and formatted correctly
            # 5#hello5#world
        
        print(encoded)
        
        return encoded

    def decode(self, s: str) -> List[str]:
        results_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # get the integer from up to the hashtag

            length_of_string = int(s[i:j])

            word = s[j+1:j+1+length_of_string]
            results_list.append(word)

            i = j + 1 + length_of_string

        return results_list