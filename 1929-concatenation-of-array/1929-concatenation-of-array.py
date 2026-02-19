class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # O(n)
        # O(n)
        # n = len(nums)
        # ans = []
        # for i in range(n):
        #     ans[i] = nums[i]
        # for i in range(n):
        #     ans[i + n] = nums[i]
        # return ans

        # O(n)
        # O(n)
        ans = []
        n = len(nums)
        for i in range(2 * n):
            ans.append(nums[i % n])
        
        return ans

        # O(n)
        # O(n)
        # return nums + nums
