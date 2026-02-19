class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # O(n^2)
        # O(1)
        n = len(nums)
        ans = []
        for i in range(n):
            total = 0
            for j in range(i + 1):
                total += nums[j]
            ans.append(total)
        return ans

        # O(n)
        # O(1)
        # prefix = 0
        # n = len(nums)
        # ans = []
        # for num in nums:
        #     prefix += num
        #     ans.append(prefix)
        
        # return ans
