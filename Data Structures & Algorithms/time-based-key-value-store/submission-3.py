class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d or self.d[key][0][1] > timestamp:
            return ""
        
        values = self.d[key]
        l, r = 0, len(values) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1
                
        return values[r][0]

