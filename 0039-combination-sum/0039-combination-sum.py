class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # n = len(candidates)
        # T = target
        # m = min(candidates)
        # O(n^(T/m))
        # O(k × T/m)

        results = []
        path = []

        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                results.append(path[:])
                return
            
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, remain - candidates[i])
                path.pop()
        
        dfs(0, target)
        return results