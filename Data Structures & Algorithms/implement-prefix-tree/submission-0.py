class TrieNode:
    def __init__(self):
        self.word = [None] * 26
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
 
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.word[idx] is None:
                cur.word[idx] = TrieNode()
            cur = cur.word[idx]
        cur.is_word = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.word[idx] is None:
                return False
            cur = cur.word[idx]
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if cur.word[idx] is None:
                return False
            cur = cur.word[idx]
        return True
        
        