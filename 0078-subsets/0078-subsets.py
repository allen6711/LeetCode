class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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