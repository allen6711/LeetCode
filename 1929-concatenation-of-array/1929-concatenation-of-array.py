class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(2 * n):
            ans.append(nums[i % n])
        
        return ans














        ans = []
        for i in range(len(nums)):
            for i in range(len(nums)):
                ans.append(nums[i])
        
        return ans