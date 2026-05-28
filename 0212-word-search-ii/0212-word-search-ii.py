class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word
        
        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            ch = board[r][c]

            # If current character is not a valid next Trie path, stop.
            if ch not in node.children:
                return
            
            next_node = node.children[ch]

            # If this Trie node stores a word, we found one.
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None      # Avoid duplicate results
            
            # Mark current cell as visited
            board[r][c] = "#"

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] != "#":
                    dfs(nx, ny, next_node)

            # Restore current cell
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result 
        