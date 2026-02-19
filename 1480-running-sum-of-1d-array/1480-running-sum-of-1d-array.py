class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        n = len(nums)
        ans = []
        for num in nums:
            prefix += num
            ans.append(prefix)
        
        return ans
