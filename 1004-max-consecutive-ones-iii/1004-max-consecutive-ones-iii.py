class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        best = float('-inf')
        zeros = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            window_len = right - left + 1
            best = max(best, window_len)
        return best
        # O(n^2)
        # O(1)
        # n = len(nums)
        # best = 0
        # for i in range(n):
        #     zeros = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zeros += 1
        #         if zeros > k:
        #             break
                
        #         window_len = j - i + 1
        #         if window_len > best:
        #             best = window_len
        # return best
        # O(n)
        # O(1)
        left = 0
        n = len(nums)
        best = float('-inf')
        zeros = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            window_len = right - left + 1
            best = max(best, window_len)
        return best