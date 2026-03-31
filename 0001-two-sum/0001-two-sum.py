class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        count = {}
        n = len(nums)
        for i in range(n):
            new_target = target - nums[i]
            if new_target in count:
                return [count[new_target], i]
            count[nums[i]] = i
                













        # O(n^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []

        # O(n)
        n = len(nums)
        visited = {}
        for i in range(n):
            if (target - nums[i]) in visited:
                return [visited[target - nums[i]], i]
            visited[nums[i]] = i

        return []