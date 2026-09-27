class TireNode:
    def __init__(self):
        self.word = [None] * 26
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TireNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.word[idx] is None:
                cur.word[idx] = TireNode()
            cur = cur.word[idx]
        cur.is_word = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            cur, idx = stack.pop()
            if idx == len(word):
                if cur.is_word:
                    return True
                continue
            elif word[idx] == '.':
                for c in cur.word:
                    if c is not None:
                        stack.append([c, idx+1])
            elif cur.word[ord(word[idx])-ord('a')] is not None:
                stack.append([cur.word[ord(word[idx])-ord('a')], idx+1])
        return False

