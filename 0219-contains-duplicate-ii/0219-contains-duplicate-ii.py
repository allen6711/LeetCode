class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # O(n^2)
        # O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j] and abs(j - i) <= k:
        #             return True
        # return False
        
        # O(n)
        # O(n)
        visited = {}
        for i, num in enumerate(nums):
            if num in visited and abs(i - visited[num]) <= k:
                return True
            visited[num] = i
        
        return False