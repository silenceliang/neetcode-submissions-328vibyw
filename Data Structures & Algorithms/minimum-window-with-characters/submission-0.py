class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # an available rolling window
        # shift left pointer when a new result comes up
        # new result -> all frequencies are matched 
        # try to minimize the window
        # keep track on min window
        freq = Counter(t)
        res = ""
        min_window = len(t)
        l = 0
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    min_window-=1
                freq[s[r]]-=1
                
            while min_window == 0:
                # hit a result
                if not res or r-l+1 < len(res):
                    res = s[l:r+1]
                if s[l] in freq:
                    if freq[s[l]] >= 0:
                        min_window += 1
                    freq[s[l]] += 1
                l+=1

        return res