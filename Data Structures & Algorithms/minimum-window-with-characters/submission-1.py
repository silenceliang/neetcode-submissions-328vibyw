class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # maintain a frequency table for keeping track target t
        freq = Counter(t)
        # to avoid checking freq everytime
        # once min_window = 0, valid substring comes up
        min_window = len(t)
        # the minimum substring
        res = ""
        # keep track over a sliding window from left to right
        l = 0

        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    min_window-=1
                freq[s[r]]-=1
            
            while min_window == 0:
                if not res or len(res) > r-l+1:
                    res = s[l:r+1]
                if s[l] in freq:
                    if freq[s[l]] >= 0:
                        # if left ptr moves forward, increament min_window when freq table is contributed  
                        min_window+=1
                    freq[s[l]]+=1
                l+=1

        return res
        