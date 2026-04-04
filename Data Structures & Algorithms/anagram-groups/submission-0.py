class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # indexing: (26)key: arr idx
        # tuple(0,..,0:26):idx
        # group by key
        # sort: O(n)*O*(26log26)
        # O(n)*O(26)+O(n)
        N = len(strs)
        group = defaultdict(list)
        for i in range(N):
            key = [0] * 26
            for c in strs[i]:
                key[ord(c)-ord('a')] += 1
            group[tuple(key)].append(i)
        return [[strs[i] for i in v_lst] for v_lst in group.values()]