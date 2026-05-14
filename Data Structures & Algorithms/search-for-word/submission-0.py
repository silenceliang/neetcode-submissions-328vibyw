class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, w = len(board), len(board[0])
        visited = [[False]*w for _ in range(r)]
        def backtrack(i, j, visited, next_word):
            if not next_word:
                return True

            if i < 0 or i >= r or j < 0 or j >= w or visited[i][j] or board[i][j] != next_word[0]:
                return False

            visited[i][j] = True
            res = backtrack(i+1,j,visited, next_word[1:]) or \
            backtrack(i-1,j,visited, next_word[1:]) or \
            backtrack(i,j+1,visited, next_word[1:]) or \
            backtrack(i,j-1,visited, next_word[1:])
            visited[i][j] = False
            return res

        return any(backtrack(i, j, visited, word) for i in range(r) for j in range(w))

        