class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        left = 0
        for i in range(len(nums)):
            if nums[i] not in visited:
                nums[left] = nums[i]
                left += 1

            visited.add(nums[i])
        return len(visited)
