class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in last:
                l = max(last[s[r]]+1, l)

            longest = max(longest, r-l+1)
            last[s[r]] = r
        
        return longest