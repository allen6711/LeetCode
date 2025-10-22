class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, subset, combinations):
        combinations.append(list(subset))
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, combinations)
            subset.pop()
    













    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)

    #     return combinations

    # def dfs(self, nums, index, subset, combinations):
    #     combinations.append(list(subset))
        
    #     for i in range(index, len(nums)):
    #         subset.append(nums[i])
    #         self.dfs(nums, i + 1, subset, combinations)
    #         subset.pop()



    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)

    #     return combinations
    
    # def dfs(self, nums, index, subset, combinations):
    #     combinations.append(list(subset))

    #     for i in range(index, len(nums)):
    #         subset.append(nums[i])
    #         self.dfs(nums, i + 1, subset, combinations)
    #         subset.pop()

    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)

    #     return combinations
    
    # def dfs(self, nums, index, subset, combinations):
    #     combinations.append(list(subset))

    #     for i in range(index, len(nums)):
    #         subset.append(nums[i])
    #         self.dfs(nums, i + 1, subset, combinations)
    #         subset.pop()

    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)

    #     return combinations

    # def dfs(self, nums, index, subset, combinations):
    #     combinations.append(list(subset))

    #     for i in range(index, len(nums)):
    #         subset.append(nums[i])
    #         self.dfs(nums, i + 1, subset, combinations)
    #         subset.pop()
    



    #     nums = sorted(nums)
    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)

    #     return combinations
    
    # def dfs(self, nums, index, subset, combinations):
    #     combinations.append(list(subset))

    #     for i in range(index, len(nums)):
    #         subset.append(nums[i])
    #         self.dfs(nums, i + 1, subset, combinations)
    #         subset.pop()

    #     nums = sorted(nums)
    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)

    #     return combinations

    
    # def dfs(self, nums, index, combination, combinations):
    #     combinations.append(list(combination))

    #     for i in range(index, len(nums)):
    #         combination.append(nums[i])

    #         self.dfs(nums, i + 1, combination, combinations)
    #         combination.pop()