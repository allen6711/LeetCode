class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(start):
            ans.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return ans
            













        # O(n*2^n)
        # O(n*2^n)
        result = []
        n = len(nums)
        def backtracking(start, path):
            result.append(path[:])

            for i in range(start, n):
                path.append(nums[i])
                
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return result