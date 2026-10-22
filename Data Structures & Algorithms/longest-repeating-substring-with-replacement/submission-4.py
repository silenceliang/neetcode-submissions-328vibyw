class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maximum = 0
        h = defaultdict(int)
        
        for r in range(len(s)):
            h[s[r]]+=1
            maximum = max(maximum, h[s[r]])
            while r-l+1-maximum > k:
                h[s[l]]-=1
                l+=1

        return len(s)-l