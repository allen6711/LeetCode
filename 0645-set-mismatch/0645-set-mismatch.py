class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
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

