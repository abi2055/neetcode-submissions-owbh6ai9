class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # handle edge cases

        characters_t = {}
        characters_window = {}

        for ch in t:
            characters_t[ch] = characters_t.get(ch, 0) + 1

        want = 0
        need = len(characters_t)

        # looking for min so start at biggest possible value
        best_result_len = float("infinity")
        best_result = [-1, -1]
        len_window = 0

        lp = 0

        for r in range(len(s)):
            characters_window[s[r]] = characters_window.get(s[r], 0) + 1

            if s[r] in characters_t and characters_window[s[r]] == characters_t[s[r]]:
                want += 1

            while want == need:
                if (r - lp + 1) < best_result_len:
                    best_result = [lp, r]
                    best_result_len = r - lp + 1
                
                # remove from left side
                characters_window[s[lp]] -= 1
                if s[lp] in characters_t and characters_window[s[lp]] < characters_t[s[lp]]:
                    want -= 1

                lp += 1

        start, end = best_result

        if best_result_len != float("infinity"):
            return s[start:end+1]
        else:
            return ""
                

        
