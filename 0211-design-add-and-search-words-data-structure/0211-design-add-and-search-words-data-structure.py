class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # l: length of word
    # O(l)
    # O(l)
    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]
        
        cur.is_word = True

    # O(l) without ".", O(26^l) with "."
    # O(l)
    def search(self, word: str) -> bool:

        def dfs(index: int, node: TrieNode) -> bool:
            # If we have checked all characters
            # the current node must be the end of a complete word.
            if index == len(word):
                return node.is_word
            
            ch = word[index]

            # Case 1: normal charachter
            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])
            
            # Case 2: wildcard "."
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True
            
            return False
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)