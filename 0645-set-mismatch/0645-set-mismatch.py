class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # O(n)
        # O(1)
        duplicate = -1
        missing = -1
        n = len(nums)

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        
        return [duplicate, missing]
        # o(n)
        # O(n)
        visited = set()
        duplicate = -1
        n = len(nums)

        for num in nums:
            if num in visited:
                duplicate = num
            else:
                visited.add(num)
        
        for num in range(1, n + 1):
            if num not in visited:
                return [duplicate, num]
        
        return []

