class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = Counter(s1)
        need = len(m)

        for i in range(len(s2)):
            cur_m = {}
            cur_need = 0
            for j in range(i, len(s2)):
                cur_m.setdefault(s2[j], 0)
                m.setdefault(s2[j], 0)
                cur_m[s2[j]] += 1
                if m[s2[j]] < cur_m[s2[j]]:
                    break
                if m[s2[j]] == cur_m[s2[j]]:
                    cur_need += 1
                if cur_need == need:
                    return True

        return False
