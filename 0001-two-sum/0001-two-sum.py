class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect = {}
        for i, num in enumerate(nums):
            new_target = target - num
            if new_target in collect:
                return [collect[new_target], i]
            collect[num] = i
        
        return -1














        # O(n^2)
        # O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []

        # O(n)
        # O(n)
        n = len(nums)
        visited = {}
        for i in range(n):
            if (target - nums[i]) in visited:
                return [visited[target - nums[i]], i]
            visited[nums[i]] = i

        return []