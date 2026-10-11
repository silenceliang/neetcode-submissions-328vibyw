class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        def find(x):
            if root[x] == x:
                return x
            return find(root[x])
        
        def union(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                root[px] = py
        
        for a, b in edges:
            union(a,b)

        res = set()
        for i in root:
            res.add(find(i))
        
        return len(res)
        