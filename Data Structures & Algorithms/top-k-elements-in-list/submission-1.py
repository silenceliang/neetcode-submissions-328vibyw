class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort
        # heap
        # 2 bucket list
        freq_bucket = [[] for _ in range(len(nums)+1)]
        freq = Counter(nums)
        for val, c in freq.items():
            freq_bucket[c].append(val)
        res = []
        for i in range(len(freq_bucket)-1, -1, -1):
            if len(freq_bucket[i]) > 0:
                res += freq_bucket[i]
            if len(res) == k:
                break
        return res