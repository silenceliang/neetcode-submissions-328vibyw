class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(s+t)+O(26)
        m = [0] * 26
        for c in s:
            m[ord(c)-ord('a')]+=1
        for c in t:
            m[ord(c)-ord('a')]-=1
        for i in range(26):
            if m[i] != 0:
                return False
        return True