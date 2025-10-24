class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combinations = []
        self.visited = set()
        self.dfs(nums, 0, [], combinations)

        return combinations

    def dfs(self, nums, index, subset, combinations):
        key = tuple(subset)

        if key not in self.visited:
            combinations.append(list(subset))
            self.visited.add(key)
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, combinations)
            subset.pop()
















    #     nums.sort()
    #     self.visited = set()
    #     combinations = []
    #     self.dfs(nums, [], 0, combinations)

    #     return combinations

    # def dfs(self, nums, subset, index, combinations):
    #     key = tuple(subset)
    #     if key not in self.visited:
    #         combinations.append(list(subset))
    #         self.visited.add(key)
        
    #     for i in range(index, len(nums)):
    #         subset.append(nums[i])
    #         self.dfs(nums, subset, i + 1, combinations)
    #         subset.pop()


        # def dfs(start_index, current_subset):
        #     result.append(current_subset[:])
        #     for index in range(start_index, len(nums)):
        #         if index != start_index and nums[index] == nums[index - 1]:
        #             continue
                
        #         current_subset.append(nums[index])
        #         dfs(index + 1, current_subset)
        #         current_subset.pop()
        # result = []
        # nums.sort()
        # dfs(0, [])
        # return result