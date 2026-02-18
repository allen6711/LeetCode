class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []














        # visited = {}
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in visited:
        #         return [visited[diff], i]

        #     visited[num] = i
        
        # return []