class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set()
        n = len(nums)
        for num in nums:
            visited.add(num)
        
        for i in range(1, n + 1):
            if i > 0 and i not in visited:
                return i















        # O(n)
        # O(n)
        # num_set = set(nums)
        # x = 1
        # while x in num_set:
        #     x += 1
        # return x
        # O(n)
        # O(1)
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n:
                correct_idx = nums[i] - 1
                if nums[correct_idx] == nums[i]:
                    break
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
                
