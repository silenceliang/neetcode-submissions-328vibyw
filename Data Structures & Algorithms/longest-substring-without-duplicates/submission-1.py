class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        h = defaultdict(int)
        res = 0
        for r in range(len(s)):
            while h[s[r]] > 0:
                h[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            h[s[r]] += 1

        return res