from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        window = len(s1)  # Represents characters still needed
        freq = Counter(s1)
        l = 0
        
        for r in range(len(s2)):
            char = s2[r]
            
            # If the character is in s1, use it up
            if char in freq:
                if freq[char] > 0:
                    window -= 1
                freq[char] -= 1
            
            # If our window exceeds len(s1), shrink from the left
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in freq:
                    if freq[left_char] >= 0:
                        window += 1
                    freq[left_char] += 1
                l += 1
                
            # If all characters matched, we found a permutation
            if window == 0:
                return True
                
        return False