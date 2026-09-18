class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # k: length of slice
        # O(nk)
        # O(k)
        # ans = []
        # left = 0
        # cur_max = float('-inf')
        # n = len(nums)
        # for right in range(k - 1, n):
        #     cur_max = max(nums[left:right + 1])
        #     ans.append(cur_max)
        #     left += 1
        
        # return ans
        dq = deque()
        ans = []
        n = len(nums)
        for right in range(n):
            # Remove the index out of window
            while dq and dq[0] <= right - k:
                dq.popleft()
            
            #
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            
            dq.append(right)

            if right >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans