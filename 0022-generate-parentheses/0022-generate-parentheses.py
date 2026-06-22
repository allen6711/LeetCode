class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # O(n * C_n)
        # O(n * C_n)
        results = []
        path = []

        def dfs(open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                results.append("".join(path))
                return
            
            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count)
                path.pop()
            
            if close_count < open_count:
                path.append(")")
                dfs(open_count, close_count + 1)
                path.pop()
        
        dfs(0, 0)
        return results