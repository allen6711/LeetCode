class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(start, remaining):
            if remaining == 0:
                ans.append(path[:])
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return ans













        # O(n2^n)
        # Auxiliary: O(n)
        # O(n2^n)
        path = []
        ans = []
        def backtrack(start, remaining):
            total = 0
            if remaining == 0:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return ans