class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort each word in the list using ASCII value
        # take the index of each word in the unchanged list 
        # map it to another list of buckets 

        keys = []      # holds the unique sorted keys
        buckets = []   # parallel list of lists for grouped anagrams

        for word in strs:
            sig = ''.join(sorted(word))   # signature (e.g., "eat" -> "aet")

            if sig in keys:               # check if we've seen this key
                idx = keys.index(sig)     # find index of existing key
                buckets[idx].append(word)
            else:
                keys.append(sig)          # new key
                buckets.append([word])    # new bucket
        
        return buckets
                
