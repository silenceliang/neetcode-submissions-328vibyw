class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain = ""
        for c in s:
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
                plain += c.lower()

        return plain == plain[::-1]