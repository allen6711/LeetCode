class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)

        return combinations

    
    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])

            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()