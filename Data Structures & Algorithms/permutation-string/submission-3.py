class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = 26*[0]
        s2_counter = 26*[0]
        # fill in window in exact length of s1
        for i in range(len(s1)):
            s1_counter[ord(s1[i])-ord('a')] += 1
            s2_counter[ord(s2[i])-ord('a')] += 1
        
        # before moving, check if it matches all
        matches = 0
        for i in range(26):
            matches += 1 if s1_counter[i] == s2_counter[i] else 0
        
        l = 0
        for i in range(len(s1), len(s2)):
            # move window
            if matches == 26: return True

            idx = ord(s2[i]) - ord('a')
            s2_counter[idx] += 1
            if s2_counter[idx] == s1_counter[idx]:
                matches += 1
            elif s2_counter[idx]-1 == s1_counter[idx]:
                # matched before
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            s2_counter[idx] -= 1
            if s2_counter[idx] == s1_counter[idx]:
                matches += 1
            elif s2_counter[idx]+1 == s1_counter[idx]:
                # matched before
                matches -= 1
            l+=1
        return matches == 26
