class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(cur, op, close, res):
            if len(cur) == 2 * n:
                res.append(cur)
                return 
            if op < n:
                backtrack(cur+"(", op+1, close, res)
            if op > close:
                backtrack(cur+')', op, close+1, res)
            
        res = []
        backtrack("", 0, 0, res)
        return res