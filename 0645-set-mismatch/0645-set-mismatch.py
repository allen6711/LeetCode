class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = set()
        n = len(nums)
        duplicate = -1

        for num in nums:
            if num in visited:
                duplicate = num

            visited.add(num)
        
        for num in range(1, n + 1):
            if num not in visited:
                return [duplicate, num]












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

